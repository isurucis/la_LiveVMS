from django.db import models
from django.contrib.auth.models import User  # Import User model
from mptt.models import MPTTModel, TreeForeignKey
from vendors.models import Vendor

# Create your models here.
class ProductCategory(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, null=True, blank=True)
    family = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    length = models.CharField(max_length=255, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, to_field='vendor_id')  # Explicitly reference vendor_id
    vendor_code = models.CharField(max_length=50, null=True, blank=True)
    cis_code = models.CharField(max_length=50, null=True, blank=True)
    laq_code = models.CharField(max_length=50, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_date = models.DateTimeField(auto_now=True)  # Automatically updates on save
    updated_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to User model

    def __str__(self):
        #return self.name
        return f"{self.name} - {self.cis_code}"
