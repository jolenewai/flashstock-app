from django.contrib import admin
from .models import Photographer, Album, Follower


# Register your models here.


admin.site.register(Photographer)
admin.site.register(Album)
admin.site.register(Follower)
