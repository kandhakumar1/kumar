# Generated by Django 4.1.3 on 2022-12-09 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='product_qty',
        ),
    ]
