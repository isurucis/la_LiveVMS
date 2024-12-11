from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import PurchaseOrder, PurchaseOrderItem
from .models import Shipment, ShipmentProduct
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem
    extra = 1

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('vendor', 'created_date', 'created_by')
    list_filter = ('vendor',)
    inlines = [PurchaseOrderItemInline]
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date',)

class ShipmentProductInline(admin.TabularInline):
    model = ShipmentProduct
    extra = 1

@admin.register(Shipment)
class ShipmentAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('id', 'name', 'date_of_arrival', 'airport', 'country_of_origin', 'status')
    list_filter = ('status', 'country_of_origin', 'date_of_arrival')
    search_fields = ('name', 'airport')
    inlines = [ShipmentProductInline]
    
# admin.site.site_header = "LiveVMS Admin"
# admin.site.site_title = "Live VMS"
# admin.site.index_title = "Live VMS"