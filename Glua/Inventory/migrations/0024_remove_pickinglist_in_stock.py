# Generated by Django 4.2.17 on 2025-03-08 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0023_issuedcannister_date_returned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickinglist',
            name='in_stock',
        ),
    ]
