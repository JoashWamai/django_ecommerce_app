# Generated by Django 3.2.8 on 2021-11-01 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_auto_20211101_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorName', models.CharField(blank=True, choices=[('Red', 'Red'), ('Black', 'Black'), ('Green', 'Green'), ('Blue', 'Blue')], max_length=20, null=True, verbose_name='ProductColor')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.color', verbose_name='ProductColor'),
        ),
    ]
