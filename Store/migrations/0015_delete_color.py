# Generated by Django 3.2.8 on 2021-11-01 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0014_remove_product_color'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Color',
        ),
    ]
