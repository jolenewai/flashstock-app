from django.contrib import admin
from .models import Customer, Favourite, Download

# Register your models here.


admin.site.register(Customer)
admin.site.register(Favourite)
admin.site.register(Download)
