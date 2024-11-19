from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Shipment
class ShipmentCalendarView(TemplateView):
    template_name = 'shipment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all campaigns to display on the calendar
        context['shipments'] = Shipment.objects.all()
        return context

class ShipmentDetailView(DetailView):
    model = Shipment
    template_name = 'detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include the products associated with this campaign
        context['products'] = self.object.products.select_related('shipment')
        
        return context
