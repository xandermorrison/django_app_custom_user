from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import User
from django.contrib.auth.models import Group

class MyAdminSite(admin.AdminSite):
    site_header = "Your Site Name Admin"

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('last_name', 'first_name')

admin_site = MyAdminSite(name="admin")

# Register your models here.
admin_site.register(User, CustomUserAdmin)
admin_site.register(Group)
