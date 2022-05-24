# Generated by Django 3.2.8 on 2021-11-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0020_alter_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='colorName',
            field=models.CharField(blank=True, choices=[('Red', 'Red'), ('Black', 'Black'), ('Green', 'Green'), ('Blue', 'Blue'), ('Pink', 'Pink'), ('Yellow', 'Yellow'), ('Purple', 'Purple'), ('Brown', 'Brown')], max_length=20, null=True, verbose_name='ProductColor'),
        ),
    ]