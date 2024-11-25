from django.db import models
from products.models import Product
# Create your models here.
class Campaign(models.Model):
    CAMTYPE_CHOICES = [
        ('discount', 'Discount Pricing'),
        ('code', 'Promo Code'),
        ('educational', 'Educational'),
        ('brand', 'Brand'),
    ]
    
    name = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=255,choices=CAMTYPE_CHOICES,)
    start_date = models.DateField()
    end_date = models.DateField()
    background = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.name

class CampaignProduct(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.campaign.name} - {self.product.name}"

class CampaignPromo(models.Model):
    CHANNEL_CHOICES = [
        ('email', 'Email'),
        ('fb', 'Facebook'),
        ('insta', 'Instergram'),
        ('tiktok', 'TikTok'),
        ('youtube', 'Youtube'),
        ('website', 'Website'),
        ('forum', 'Forum(R2R)'),
    ]
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign_promo')
    name = models.CharField(max_length=255)
    channel = models.CharField(max_length=50,choices=CHANNEL_CHOICES,)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} for {self.campaign.name}"
