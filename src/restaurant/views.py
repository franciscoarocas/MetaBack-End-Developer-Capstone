from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from .models import Menu, Table
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html', {})



class MenuItemsView(ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer


class BookingViewSet(ModelViewSet):
  queryset = Table.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]