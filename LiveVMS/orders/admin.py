from django.contrib import admin
from .models import PurchaseOrder, PurchaseOrderItem
from .models import Shipment, ShipmentProduct

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

class ShipmentProductInline(admin.TabularInline):
    model = ShipmentProduct
    extra = 1

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_arrival', 'airport', 'country_of_origin', 'status')
    list_filter = ('status', 'country_of_origin', 'date_of_arrival')
    search_fields = ('name', 'airport')
    inlines = [ShipmentProductInline]
    
admin.site.site_header = "LiveVMS Admin"
admin.site.site_title = "Live VMS"
admin.site.index_title = "Live VMS"