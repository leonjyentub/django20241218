from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Message

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'nickname', 'birthday', 'address', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname', 'bio', 'birthday', 'address', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname', 'bio', 'birthday', 'address', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)