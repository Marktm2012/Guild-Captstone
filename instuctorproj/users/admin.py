from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday','bio', 'location', 'phone_number', 'is_instructor', 'enrollments')}),
    )

admin.site.register(User, CustomUserAdmin)