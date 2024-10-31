from django.contrib import admin
from .models import PurchaseOrder, PurchaseOrderItem

class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem
    extra = 1

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'created_date', 'created_by')
    list_filter = ('vendor',)
    inlines = [PurchaseOrderItemInline]
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date',)
