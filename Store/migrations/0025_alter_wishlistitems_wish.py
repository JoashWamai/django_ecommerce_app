# Generated by Django 3.2.8 on 2021-12-15 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0024_auto_20211213_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitems',
            name='wish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Store.wishlist', verbose_name='order'),
        ),
    ]
