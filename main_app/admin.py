from django.contrib import admin

# Register your models here.
from .models import Aircraft, Maintainance, Airbase, Photo

admin.site.register(Aircraft)
admin.site.register(Maintainance)
admin.site.register(Airbase)
admin.site.register(Photo)