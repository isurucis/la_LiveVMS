from django.db import models
from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import  Campaign, CampaignProduct, CampaignPromo
from .forms import CampaignForm 
from unfold.admin import StackedInline, TabularInline
from unfold.contrib.forms.widgets import WysiwygWidget
from django.utils.html import format_html


class CampaignProductInline(TabularInline):
    model = CampaignProduct
    extra = 0
    tab = True
    raw_id_fields= ["product",]
    
    def get_readonly_fields(self, request, obj=None):
        return ('product_stock', 'product_price', 'new_discounted_price', 'short_qty') + self.readonly_fields

    def product_stock(self, obj):
        return obj.product_stock()

    def product_price(self, obj):
        return obj.product_price()

    def new_discounted_price(self, obj):
        #return format_html('<span>${:.2f}</span>', obj.new_discounted_price()) if obj.new_discounted_price() != 'N/A' else 'N/A'
        return obj.new_discounted_price()

    def short_qty(self, obj):
        return obj.short_qty()

    product_stock.short_description = 'Stock'
    product_price.short_description = 'Price'
    new_discounted_price.short_description = 'Discounted Price'
    short_qty.short_description = 'Short Quantity'

    fields = ('product', 'product_stock', 'product_price', 'qty_required', 'discount', 'new_discounted_price', 'short_qty')
    

class CampaignPromolInline(StackedInline):
    formfield_overrides = {
        models.TextField: {
            'widget': WysiwygWidget,
            #'initial': "<b>BACKGROUND</b><ul><li>point one</li></ul> <b>EXPECTED KPIs</b><ul><li>point one</li></ul> <b>SEGMENTATION</b><ul><li>point one</li></ul> <b>MESSAGES</b><ul><li>point one</li></ul> <b>LOOK & FEEL</b><ul><li>point one</li></ul>",
        }
    }
    model = CampaignPromo
    extra = 0
    tab = True

@admin.register(Campaign)
class CampaignAdmin(ModelAdmin):
    form = CampaignForm
    list_display = ('name', 'campaign_type', 'start_date', 'end_date')
    inlines = [CampaignProductInline, CampaignPromolInline]
    search_fields = ('name', 'campaign_type')
    date_hierarchy = 'start_date'


# admin.site.site_header = "LiveVMS Admin"
# admin.site.site_title = "Live VMS"
# admin.site.index_title = "Live VMS"