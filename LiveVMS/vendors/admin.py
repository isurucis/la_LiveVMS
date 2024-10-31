from django.contrib import admin
from .models import Vendor
from products.models import Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'address')
    
    inlines = [ProductInline] 
