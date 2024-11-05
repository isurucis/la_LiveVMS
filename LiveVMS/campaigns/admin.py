from django.contrib import admin
from .models import  Campaign, CampaignProduct, CampaignChannel

class CampaignProductInline(admin.TabularInline):
    model = CampaignProduct
    extra = 1

class CampaignChannelInline(admin.TabularInline):
    model = CampaignChannel
    extra = 1

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign_type', 'start_date', 'end_date')
    inlines = [CampaignProductInline, CampaignChannelInline]
    search_fields = ('name', 'campaign_type')
    date_hierarchy = 'start_date'


admin.site.site_header = "LiveVMS Admin"
admin.site.site_title = "Live VMS"
admin.site.index_title = "Live VMS"