from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=False, null=False)
    url = models.URLField(blank=False)
    tags = models.ManyToManyField('Tag')
    category = models.ManyToManyField('Category')
    owner = owner = models.ForeignKey(
        User,
        on_delete='CASCADE',
        limit_choices_to={'1': 'Photographer'}
    )

    def __str__(self):
        return self.id + '_' + self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
