# Generated by Django 4.2.16 on 2024-11-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0004_alter_campaign_campaign_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaignpromo",
            name="schedule_date",
            field=models.DateTimeField(),
        ),
    ]