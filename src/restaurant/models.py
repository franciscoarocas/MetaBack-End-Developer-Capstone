from django.db import models

# Create your models here.
class Menu(models.Model):

  name = models.CharField(max_length=256)
  No_of_guest = models.IntegerField()
  BookingDate = models.DateTimeField()


class Table(models.Model):

  Title = models.CharField(max_length=256)
  Price = models.DecimalField(max_digits=10, decimal_places=2)
  Inventory = models.IntegerField()