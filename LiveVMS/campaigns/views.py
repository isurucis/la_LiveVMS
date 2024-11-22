from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Campaign
class CampaignCalendarView(TemplateView):
    template_name = 'campaigns/calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all campaigns to display on the calendar
        context['campaigns'] = Campaign.objects.all()
        return context

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'campaigns/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include the products associated with this campaign
        context['products'] = self.object.campaign_products.select_related('product')
        return context
