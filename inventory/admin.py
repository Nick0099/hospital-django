from django.contrib import admin
from .models import InventoryItem, Supplier

# Register your models here.
@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'supplier', 'reorder_level','expiry_date','category')
    list_filter   = ('category', 'supplier')
    search_fields = ('name',)

admin.site.register(Supplier)
