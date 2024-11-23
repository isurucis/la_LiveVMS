from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export import resources
from .models import Vendor
from products.models import Product
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from unfold.admin import StackedInline, TabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group



admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
class ProductInline(TabularInline):
    model = Product
    extra = 1
    tab = True
    readonly_fields = ('created_date', 'updated_date', 'updated_person')
class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor
        fields = ('name', 'etf_vendor_code', 'vendor_id', 'country', 'status')
        import_id_fields = ('vendor_id',)

@admin.register(Vendor)
class VendorAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = VendorResource
    list_display = ('name', 'etf_vendor_code', 'vendor_id', 'country', 'status')
    list_filter = ('country', 'status')
    search_fields = ('name', 'etf_vendor_code', 'vendor_id')
    inlines = [ProductInline]
    
    # Unfold specific configurations (optional)
    # unfold_config = {
    #     'list_per_page': 25,  # Adjust list items per page
    #     'search': {'placeholder': 'Search vendors...'},  # Customize search bar placeholder
    # }

# admin.site.site_header = "LiveVMS Admin"
# admin.site.site_title = "Live VMS"
# admin.site.index_title = "Live VMS"

