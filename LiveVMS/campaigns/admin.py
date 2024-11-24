from django.db import models
from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import  Campaign, CampaignProduct, CampaignPromo
from .forms import CampaignForm 
from unfold.admin import StackedInline, TabularInline
from unfold.contrib.forms.widgets import WysiwygWidget


class CampaignProductInline(TabularInline):
    model = CampaignProduct
    extra = 1
    tab = True
    raw_id_fields= ["product",]

class CampaignPromolInline(TabularInline):
    model = CampaignPromo
    extra = 1
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