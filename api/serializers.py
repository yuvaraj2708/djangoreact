from rest_framework import serializers
from .models import Contact
from django.contrib.auth import get_user_model

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ('user', )

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )