from django.contrib import admin
from .models import ProductCategory, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin


    

class ProductCategoryResource(resources.ModelResource):

    class Meta:
        model = ProductCategory
        fields = ('name', 'parent',)
        # Optional: Exclude fields you don't want to import/export (e.g., 'id')
        # exclude = ('id',)
        import_id_fields = ('name',)  # Use 'name' as the identifier for import


@admin.register(ProductCategory)
class ProductCategoryAdmin(ImportExportModelAdmin, DraggableMPTTAdmin):
    resource_class = ProductCategoryResource
    list_display = ('id','name',)



class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'name', 'scientific_name', 'category', 'vendor', 'vendor_code', 'cis_code', 'laq_code', 'stock', 'price', 'is_active',)  # Specify the fields to import/export

class CategoryFilter(admin.SimpleListFilter):
    title = 'category'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        categories = ProductCategory.objects.all()
        return [(cat.id, cat.name) for cat in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('id','name', 'scientific_name', 'category', 'vendor', 'stock', 'price', 'is_active', 'created_date')
    list_filter = (CategoryFilter, 'vendor', 'is_active')
    search_fields = ('name', 'scientific_name', 'vendor_code', 'cis_code', 'laq_code')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date',)

admin.site.site_header = "LiveVMS Admin"
admin.site.site_title = "Live VMS"
admin.site.index_title = "Live VMS"