from django.contrib import admin
from .models import Items, CustomUser

# Register your models here.
admin.site.register(Items)
admin.site.register(CustomUser)