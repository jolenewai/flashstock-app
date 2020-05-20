from django.db import models
from home.models import Person

# Create your models here.


class Customer(Person):
    pass


class Download(models.Model):
    photo = models.ForeignKey('photos.Photo', on_delete='CASCADE')
    owner = models.ForeignKey(Customer, on_delete='CASCADE')
    date_download = models.DateField(auto_now_add=True)


class Favourite(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ForeignKey('photos.Photo', on_delete='CASCADE')
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Customer, on_delete='CASCADE')
