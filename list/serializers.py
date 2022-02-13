from dataclasses import field
import imp
from pyexpat import model
from .models import Home  
from rest_framework import serializers 


class HomeSerializer(serializers.ModelSerializer):
    model = Home
    fields = ('id', 'tittle', 'description')
