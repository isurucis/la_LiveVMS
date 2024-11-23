from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import  Campaign, CampaignProduct, CampaignChannel
from unfold.admin import StackedInline, TabularInline

class CampaignProductInline(TabularInline):
    model = CampaignProduct
    extra = 1
    tab = True
    raw_id_fields= ["product",]

class CampaignChannelInline(TabularInline):
    model = CampaignChannel
    extra = 1
    tab = True

@admin.register(Campaign)
class CampaignAdmin(ModelAdmin):
    list_display = ('name', 'campaign_type', 'start_date', 'end_date')
    inlines = [CampaignProductInline, CampaignChannelInline]
    search_fields = ('name', 'campaign_type')
    date_hierarchy = 'start_date'


# admin.site.site_header = "LiveVMS Admin"
# admin.site.site_title = "Live VMS"
# admin.site.index_title = "Live VMS"