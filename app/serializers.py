from rest_framework import serializers
from .models import *

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = ['username', 'password']