from django.contrib import admin
from .models import Profile, GroomProfile, BrideProfile

# Register your models here.

admin.site.register(Profile)
admin.site.register(GroomProfile)
admin.site.register(BrideProfile)