from orders.models import Shipment
from campaigns.models import Campaign, CampaignPromo

# utils.py
def dashboard_callback(request, context):
    context.update({
        "campaigns": Campaign.objects.all(),
        "schedules": CampaignPromo.objects.all(),
        "shipments": Shipment.objects.all(),
        
    })

    return context
