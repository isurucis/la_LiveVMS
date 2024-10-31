from django.contrib import admin
from .models import Vendor, ProductCategory, Product, PurchaseOrder, PurchaseOrderItem, Campaign, CampaignProduct, CampaignChannel

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'category', 'vendor', 'stock', 'price', 'is_active', 'created_date')
    list_filter = ('category', 'vendor', 'is_active')
    search_fields = ('name', 'scientific_name', 'vendor_code', 'cis_code', 'laq_code')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date',)

