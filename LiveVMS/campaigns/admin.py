from django.contrib import admin
from .models import  Campaign, CampaignProduct, CampaignChannel
from .forms import CampaignProductForm

class CampaignProductInline(admin.TabularInline):
    model = CampaignProduct
    form = CampaignProductForm
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        # If the campaign has a category, pass it to the form
        if obj and obj.category:
            for form in formset.forms:
                form.fields['product'].queryset = form.fields['product'].queryset.filter(category=obj.category)
        return formset


class CampaignChannelInline(admin.TabularInline):
    model = CampaignChannel
    extra = 1

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign_type', 'start_date', 'end_date')
    inlines = [CampaignProductInline, CampaignChannelInline]
    search_fields = ('name', 'campaign_type')
    date_hierarchy = 'start_date'

