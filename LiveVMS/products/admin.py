from django.contrib import admin
from .models import ProductCategory, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('name', 'scientific_name', 'category', 'vendor', 'vendor_code', 'cis_code', 'laq_code', 'stock', 'price', 'is_active',)  # Specify the fields to import/export
        
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('name', 'scientific_name', 'category', 'vendor', 'stock', 'price', 'is_active', 'created_date')
    list_filter = ('category', 'vendor', 'is_active')
    search_fields = ('name', 'scientific_name', 'vendor_code', 'cis_code', 'laq_code')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date',)

