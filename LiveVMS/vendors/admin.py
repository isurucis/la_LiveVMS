from django.contrib import admin
from import_export import resources
from .models import Vendor
from products.models import Product
from import_export.admin import ImportExportModelAdmin

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor
        fields = ('name', 'etf_vendor_code', 'vendor_id', 'country', 'status')
        import_id_fields = ('vendor_id',)

@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    resource_class = VendorResource
    list_display = ('name', 'etf_vendor_code', 'vendor_id', 'country', 'status')
    list_filter = ('country', 'status')
    search_fields = ('name', 'etf_vendor_code', 'vendor_id')
    inlines = [ProductInline]

admin.site.site_header = "LiveVMS Admin"
admin.site.site_title = "Live VMS"
admin.site.index_title = "Live VMS"

