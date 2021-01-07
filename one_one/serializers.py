from django.contrib.auth.models import User

from .models import one
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'username',
                  'password', 'is_superuser')


class oneSerializer(serializers.ModelSerializer):
    """ A serializer for the PileColor model """
    class Meta:
        model = one
        fields = ('id', 'question', 'answer', 'comment', 'dAnswer_2', 'dAnswer_3','dAnswer_4', 'dAnswer_5')

