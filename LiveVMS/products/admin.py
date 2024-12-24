from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ProductCategory, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from unfold.contrib.filters.admin import (
    ChoicesDropdownFilter,
    MultipleRelatedDropdownFilter,
    RangeDateFilter,
    RangeDateTimeFilter,
    RangeNumericFilter,
    RelatedDropdownFilter,
    SingleNumericFilter,
    TextFilter,
)

    

# class ProductCategoryResource(resources.ModelResource):

#     class Meta:
#         model = ProductCategory
#         fields = ('name', 'parent',)
#         # Optional: Exclude fields you don't want to import/export (e.g., 'id')
#         # exclude = ('id',)
#         import_id_fields = ('name',)  # Use 'name' as the identifier for import


# @admin.register(ProductCategory)
# class ProductCategoryAdmin(ImportExportModelAdmin, DraggableMPTTAdmin):
#     resource_class = ProductCategoryResource




class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'name', 'scientific_name', 'size', 'length', 'family', 'category', 'vendor', 'vendor_code', 'cis_code', 'laq_code', 'stock', 'price', 'is_active',)  # Specify the fields to import/export

# class CategoryFilter(admin.SimpleListFilter):
#     title = 'category'
#     parameter_name = 'category'

#     def lookups(self, request, model_admin):
#         categories = ProductCategory.objects.all()
#         return [(cat.id, cat.name) for cat in categories]

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(category__id=self.value())
#         return queryset

class InStockFilter(admin.SimpleListFilter):
    title = 'In Stock'
    parameter_name = 'in_stock'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'In Stock'),
            ('no', 'Out of Stock'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(stock__gt=0)
        elif self.value() == 'no':
            return queryset.filter(stock=0)
        return queryset
    
@admin.register(Product)
class ProductAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = ProductResource
    list_display = ('laq_code','cis_code', 'id', 'name', 'scientific_name', 'size', 'length', 'family', 'vendor', 'stock', 'price', 'is_active', 'updated_date')
    list_filter = ( "is_active", InStockFilter, ("family", ChoicesDropdownFilter), ("vendor", ChoicesDropdownFilter), )
    search_fields = ('name', 'scientific_name', 'vendor_code', 'cis_code', 'laq_code')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date', 'updated_date', 'updated_person')
    autocomplete_fields = ["vendor"]

# admin.site.site_header = "LiveVMS Admin"
# admin.site.site_title = "Live VMS"
# admin.site.index_title = "Live VMS"