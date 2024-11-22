from django.shortcuts import render
from orders.models import Shipment

def dashboard_callback(request, context):
    # Fetch data for your dashboard, e.g., from models or external APIs
    context['shipments'] = Shipment.objects.all()

    #return render(request, 'my_dashboard.html', context)
    return context

