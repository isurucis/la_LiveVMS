from django.db import models

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
