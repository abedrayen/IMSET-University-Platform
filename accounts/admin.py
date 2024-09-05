from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'cin_number', 'specialty', 'location_of_birth']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'cin_number']
    readonly_fields = ['date_joined', 'last_login']

admin.site.register(User, UserAdmin)
