# Generated by Django 3.2.8 on 2021-11-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0021_alter_color_colorname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brandName',
            field=models.CharField(blank=True, default='Generic', max_length=50, null=True, verbose_name='BrandName'),
        ),
    ]