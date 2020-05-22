from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'phone_number', 'purchase_number']


admin.site.register(Profile, ProfileAdmin)
