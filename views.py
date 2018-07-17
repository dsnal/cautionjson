# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect

from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse
from cautionjson.models import Trip
from cautionjson.trip import TripSerializer
from cautionjson.trip import UserSerializer
from cautionjson.permissions import IsOwnerOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from django.contrib.auth.models import User
from rest_framework import permissions
from .forms import RegistrationForm
from .serializers import UserSerializer

#List of Trips -> Return JSON API VIEW
class TripList(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def get(self, request, format=None):
		trips = Trip.objects.all()
		serializer = TripSerializer(trips, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TripSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
 
 #Trip	Detail -> Return JSON API VIEW
class TripDetail(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	def get_object(self, pk):
		try:
			return Trip.objects.get(pk=pk)
		except Trip.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
		trip = self.get_object(pk)
		serializer = TripSerializer(trip)
		return Response(serializer.data)
	def put(self, request, pk, format=None):
		trip = self.get_object(pk)
		serializer = TripSerializer(trip, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk, format=None):
		trip = self.get_object(pk)
		trip.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

#GETTING USER LIST
class UserList(generics.ListAPIView):

	def get(self, request, format=None):
		queryset = User.objects.all()
		context = {'userlist' : queryset}
		return render(request,'cautionjson/userlist.html', context)
 
#NOT WORKING YET
class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer



#TRIP LIST -> HTML PAGE RETURN

def mainpage(request):
	tripse= Trip.objects.order_by('-id')
	context = {'latest_trips' : tripse}
	return render(request, 'cautionjson/mainpage.html', context)


#TRIP INSERTION
def datainsert(request):
		return render(request,'cautionjson/datainsert.html')

#GET DATA FROM DATA INSERTION AND PUT THEM INTO MODEL, RETURN FINISH PAGE
def finish(request):
	username= request.user.username
	carnumm=request.POST.get('txtcarnum')
	lat = request.POST.get('lat')
	lon = request.POST.get('lon')
	lat1 = request.POST.get('lat1')
	lon1 = request.POST.get('lon1')
	trips = Trip(username=username,carnum=carnumm,slat=lat,slong=lon,dlat=lat1,dlong=lon1)
	trips.save()
	return render(request,'cautionjson/finish.html')
# RGISTER PAGE-> DIRECT TO LOGIN
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/trips/login')
	else:
		form = RegistrationForm()
		args = {'form':form}
		return render(request, 'cautionjson/registeration.html', args)

# LOIGN REDIRECT CAN BE FOUND PROJECT SETTING FILE
def login(request):
	return render(request,'trips/login.html')



	