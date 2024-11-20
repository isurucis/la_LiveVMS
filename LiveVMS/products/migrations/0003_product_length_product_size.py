# Generated by Django 5.1.2 on 2024-11-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_remove_product_category_product_family"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="length",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]