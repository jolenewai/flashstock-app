from django.db import models
from django.contrib.auth.models import User
from person.models import Person
from photos.models import Photo

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    photos = models.ManyToManyField(Photo)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        Person,
        on_delete='CASCADE',
        limit_choices_to={'2', 'Customer'}
    )


class Download(models.Model):
    photos = models.ManyToManyField(Photo)
    owner = models.ForeignKey(
        Person,
        on_delete='CASCADE',
        limit_choices_to={'2', 'Customer'}
    )

