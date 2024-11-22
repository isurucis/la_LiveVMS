from orders.models import Shipment
from campaigns.models import Campaign

# utils.py
def dashboard_callback(request, context):
    context.update({
        "shipments": Campaign.objects.all(),
        "campaigns": Shipment.objects.all()
    })

    return context
