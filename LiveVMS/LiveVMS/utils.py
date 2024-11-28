from django.utils.timezone import now
from datetime import date
from orders.models import Shipment
from campaigns.models import Campaign, CampaignPromo, CampaignProduct

def dashboard_callback(request, context):
    # Filter upcoming campaigns
    upcoming_campaigns = Campaign.objects.filter(start_date__gte=now())

    # Calculate product short quantity percentage for each upcoming campaign
    campaign_short_qty_data = []
    for campaign in upcoming_campaigns:
        total_qty_required = 0
        total_short_qty = 0

        for campaign_product in campaign.campaign_products.all():
            total_qty_required += campaign_product.qty_required
            total_short_qty += campaign_product.short_qty()

        if total_qty_required > 0:
            short_percentage = (total_short_qty / total_qty_required) * 100
        else:
            short_percentage = 0

        campaign_short_qty_data.append({
            "campaign": campaign,
            "short_percentage": short_percentage,
        })

    # Calculate top 30 products with the highest shortages
    all_campaign_products = CampaignProduct.objects.filter(campaign__start_date__gte=now())
    top_shortages = sorted(
        all_campaign_products,
        key=lambda cp: cp.short_qty(),
        reverse=True
    )[:30]
    today = date.today()
    # Update context
    context.update({
        "today": today,
        "campaigns": Campaign.objects.all(),
        "schedules": CampaignPromo.objects.all(),
        "shipments": Shipment.objects.all(),
        "upcoming_campaign_shortages": campaign_short_qty_data,
        "top_short_products": [{
            "product_name": cp.product.name,
            "campaign_name": cp.campaign.name,
            "qty_required": cp.qty_required,
            "short_qty": cp.short_qty(),
        } for cp in top_shortages],
    })

    return context
