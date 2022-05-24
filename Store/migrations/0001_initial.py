# Generated by Django 3.2.8 on 2021-10-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(blank=True, max_length=50, null=True, verbose_name='CategoryName')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(blank=True, max_length=225, null=True, verbose_name='CustomerName')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateField(auto_now_add=True, verbose_name='Date Ordered')),
                ('orderId', models.IntegerField(blank=True, null=True, verbose_name='OrderId')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=255, null=True, verbose_name='ProductName')),
                ('oldPrice', models.FloatField(blank=True, default=0.0, null=True, verbose_name='OldPrice')),
                ('newPrice', models.FloatField(blank=True, null=True, verbose_name='NewPrice')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='ProductColor')),
                ('size', models.CharField(choices=[('Small', 's'), ('Medium', 'm'), ('Large', 'l'), ('XLarge', 'xl')], max_length=20, verbose_name='ProductSize')),
                ('availability', models.BooleanField(verbose_name='ProductAvailability')),
                ('description', models.TextField(blank=True, null=True, verbose_name='ProductDescription')),
                ('productImage', models.ImageField(blank=True, null=True, upload_to='', verbose_name='ProductImageUrl')),
                ('ratings', models.FloatField(blank=True, null=True, verbose_name='Rating')),
            ],
        ),
    ]
