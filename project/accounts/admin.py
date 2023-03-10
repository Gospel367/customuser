from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomuserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'last_login', 'is_active')

    fieldsets = ( 
                 ( None, { 'fields': ('username', 'password') }),
                 
                 ('Personal info', { 'fields' : ('first_name', 'last_name', 'email') }),
                 
                ('Permissions', { 'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions') }),

                 ('Important dates', {'fields': ('last_login', 'date_joined') }),
                 
                 ('Additional info:', {'fields': ( 'address',  'phone_number', 'customer_id')}),
                 
                 )
    
    add_fieldsets = ( 
                     
                 ( None, { 'fields': ('username', 'password1', 'password2') }),
                 
                 ('Personal info', { 'fields' : ('first_name', 'last_name', 'email') }),
                 
                ('Permissions', { 'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions') }),
                 
                 ('Important dates', {'fields': ('last_login', 'date_joined') }),
                 
                 ('Additional info:', {'fields': ( 'address', 'phone_number', 'customer_id')}),
                 
                 )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user_email',)

admin.site.register(Customuser, CustomuserAdmin)
admin.site.register(Profile, ProfileAdmin)