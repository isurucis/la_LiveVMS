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
    qty_required = models.PositiveIntegerField(default=0, verbose_name="Quantity Required")
    discount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2, verbose_name="Discount (%)")

    def product_stock(self):
        return self.product.stock if hasattr(self.product, 'stock') else 'N/A'

    def product_price(self):
        return self.product.price if hasattr(self.product, 'price') else 'N/A'

    def new_discounted_price(self):
        if self.product_price() != 'N/A':
            discount_amount = self.product_price() * (self.discount / 100)
            return self.product_price() - discount_amount
        return 'N/A'

    def short_qty(self):
        if self.qty_required > self.product_stock():
            return self.qty_required - self.product_stock()
        return 0

    product_stock.short_description = 'Stock'
    product_price.short_description = 'Price'
    new_discounted_price.short_description = 'Discounted Price'
    short_qty.short_description = 'Short Quantity'

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
    schedule_date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} for {self.campaign.name}"
