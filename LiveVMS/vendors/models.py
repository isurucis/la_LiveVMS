from django.db import models

class Vendor(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
        ('inactive', 'Temporarily Inactive'),
        ('pending', 'Pending'),
    ]

    name = models.CharField(max_length=255, verbose_name="Vendor Name")
    etf_vendor_code = models.CharField(max_length=10, verbose_name="ETF Vendor Code")
    vendor_id = models.CharField(max_length=10, unique=True, verbose_name="Vendor ID")
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Vendor Status")

    def __str__(self):
        return self.name