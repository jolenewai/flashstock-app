from django.db import models
from home.models import Person
from customers.models import Customer

# Create your models here.


class Photographer(Person):
    pass


class Album(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=False, null=False)
    tags = models.ManyToManyField('photos.Tag')
    category = models.ManyToManyField('photos.Category')
    owner = models.ForeignKey(Photographer, on_delete='CASCADE')

    def __str__(self):
        return self.title


class Follower(models.Model):
    owner = models.ForeignKey(Photographer, on_delete='CASCADE')
    followers = models.ManyToManyField(Customer)
