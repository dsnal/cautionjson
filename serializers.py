from rest_framework import serializers
from cautionjson.models import Trip
from django.contrib.auth.models import User
class TripSerializer(serializers.ModelSerializer):
	
	class Meta:
		"""docstring for Meta"""
		model = Trip
		fields = ('id', 'username', 'carnum', 'slat', 'slong', 'dlat', 'dlong')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', )