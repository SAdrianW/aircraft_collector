from django.contrib import admin

# Register your models here.
from .models import Aircraft, Maintainance

admin.site.register(Aircraft)
admin.site.register(Maintainance)