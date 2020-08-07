from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('emailname', 'username', 'email', 'password', 'is_staff')
    fieldsets = (
        ('field', {'fields': (
            'emailname',
        )}),
    )+BaseUserAdmin.fieldsets

    add_fieldsets = (
        ('User_data', {
            'fields': ('emailname',),
        }),
    )+BaseUserAdmin.add_fieldsets

    #list_display = ('emailname')+BaseUserAdmin.list_display