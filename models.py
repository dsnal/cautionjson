# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Trip(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=200)
	carnum = models.CharField(max_length=200)
	slat = models.CharField(max_length=200)
	slong = models.CharField(max_length=200)
	dlat = models.CharField(max_length=200)
	dlong = models.CharField(max_length=200)
	highlighted = models.TextField()
	
	class Meta:
		ordering = ('created',)
			
# Create your models here.
