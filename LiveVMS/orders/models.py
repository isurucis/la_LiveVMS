from django.db import models
from vendors.models import Vendor
from products.models import Product

# Create your models here.
class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)  # Or link to a User model

    def __str__(self):
        return f"PO {self.id} for {self.vendor.name}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('transit', 'In Transit'),
        ('arrived', 'Arrived'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    name = models.CharField(max_length=255)
    date_of_arrival = models.DateField()
    airport = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.status}"

class ShipmentProduct(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=100)  # e.g., "Small", "Medium", "Large"
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.size}) - {self.quantity}"