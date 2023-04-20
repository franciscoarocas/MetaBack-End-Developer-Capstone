
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):

  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(ModelSerializer):
  pass