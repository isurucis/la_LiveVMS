# Generated by Django 4.2.16 on 2024-11-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0006_remove_campaignpromo_schedule_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaignproduct",
            name="discount",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=5, verbose_name="Discount (%)"
            ),
        ),
        migrations.AddField(
            model_name="campaignproduct",
            name="qty_required",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Quantity Required"
            ),
        ),
    ]
