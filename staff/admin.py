from django.contrib import admin
from .models import Department, Staff

# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'department', 'shift', 'is_active']
    list_filter = ['role', 'department', 'shift', 'is_active']
    search_fields = ['name', 'email']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)