# Generated by Django 3.2.9 on 2022-02-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jimmy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Sides', 'sides'), ("Chef's Special", 'specials'), ('Drinks', 'drinks'), ('Dessert', 'dessert')], max_length=50),
        ),
    ]