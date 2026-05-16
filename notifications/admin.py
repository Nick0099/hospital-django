from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'type', 'is_read', 'created_at')
    list_filter = ('is_read', 'type', 'is_sent')
    search_fields = ('patient__username', 'message')
# Register your models here.
