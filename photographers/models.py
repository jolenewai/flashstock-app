from django.db import models
from django.contrib.auth.models import User
from person.models import Person
from photos.models import Photo

# Create your models here.


class Photographer(models.Model):
    followers = models.ManyToManyField(
        Person,
        through='Follower',
        through_fields=('owner', 'followers')
    )
    albums = models.ManyToManyField('Album')
    person_id = models.ForeignKey(Person)


class Album(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=False, null=False)
    photos = models.ManyToManyField(Photo)
    tags = models.ManyToManyField('Tag')
    category = models.ManyToManyField('Category')
    owner = models.ForeignKey(
        User,
        on_delete='CASCADE',
        limit_choices_to={'1': 'Photographer'}
    )

    def __str__(self):
        return self.title


class Request(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    request_to = models.ForeignKey(
        Person,
        on_delete='CASCADE',
        limit_choices_to={'1': 'Photographer'},
        related_name='request_to_photographer'
    )
    request_from = models.ForeignKey(
        Person,
        on_delete='CASCASE',
        limit_choices_to={'2', 'Customer'},
        related_name='request_from_customer'
    )

    def __str__(self):
        return '#' + str(self.id) + ' - ' + self.title


class Follower(models.Model):
    owner = models.ForeignKey(
        Person,
        on_delete='CASCADE',
        limit_choices_to={'1': 'Photographer'},
        related_name='photographer_being_followed'
    )
    followers = models.ManyToManyField(
        Person,
        limit_choices_to={'2': 'Customer'},
        related_name='customer_following'
    )



