# Generated by Django 3.2.8 on 2021-12-04 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0022_alter_brand_brandname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True, verbose_name='Cart Completed'),
        ),
        migrations.AddField(
            model_name='product',
            name='productQuantity',
            field=models.IntegerField(default=1, verbose_name='Product Quantity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Store.customer', verbose_name='customer'),
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderQuantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Order Quantity')),
                ('dateAdded', models.DateTimeField(auto_now_add=True, verbose_name='DateTime Added')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Store.order', verbose_name='order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Store.product', verbose_name='product')),
            ],
        ),
    ]
