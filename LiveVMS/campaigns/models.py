from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class CampaignProduct(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.campaign.name} - {self.product.name}"

class CampaignChannel(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign_channels')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} for {self.campaign.name}"
