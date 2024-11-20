# Generated by Django 5.1.2 on 2024-11-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="family",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]