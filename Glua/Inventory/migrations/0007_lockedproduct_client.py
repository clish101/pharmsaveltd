# Generated by Django 3.1.2 on 2025-01-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_auto_20250101_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='lockedproduct',
            name='client',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
