from django.contrib import admin
from .models import UserProfile, Property, PropertyImage

admin.site.register(UserProfile)
admin.site.register(Property)
admin.site.register(PropertyImage)

