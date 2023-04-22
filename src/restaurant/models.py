from django.db import models

# Create your models here.
class Table(models.Model):

  name = models.CharField(max_length=256)
  no_of_guest = models.IntegerField()
  bookingDate = models.DateTimeField()


class Menu(models.Model):

  title = models.CharField(max_length=256)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.IntegerField()

  def __str__(self):
    return f'{self.title} : {str(self.price)}'