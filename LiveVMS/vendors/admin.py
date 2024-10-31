from django.contrib import admin
from .models import Vendor, ProductCategory, Product, PurchaseOrder, PurchaseOrderItem, Campaign, CampaignProduct, CampaignChannel

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'address')
