from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True
    )

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_code = models.CharField(max_length=50, null=True, blank=True)
    cis_code = models.CharField(max_length=50, null=True, blank=True)
    laq_code = models.CharField(max_length=50, null=True, blank=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=255)  # You can replace this with a ForeignKey to a User model if needed

    def __str__(self):
        return self.name
