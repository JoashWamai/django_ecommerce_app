# Generated by Django 3.2.8 on 2021-11-01 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
    ]
