from django.contrib import admin
from .models import Photo, Tag, Category

# Register your models here.


admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Category)

