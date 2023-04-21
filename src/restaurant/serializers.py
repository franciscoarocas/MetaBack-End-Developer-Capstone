
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Menu, Table

class UserSerializer(ModelSerializer):

  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(ModelSerializer):

  class Meta:
    model = Menu
    fields = "__ALL__"



class BookingSerializer(ModelSerializer):
  class Meta:
    model = Table
    fields = "__ALL__"