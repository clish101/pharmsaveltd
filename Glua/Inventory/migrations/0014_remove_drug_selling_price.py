# Generated by Django 4.2.17 on 2025-01-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0013_alter_sale_drug_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='selling_price',
        ),
    ]
