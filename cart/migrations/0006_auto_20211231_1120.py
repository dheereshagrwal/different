# Generated by Django 3.0.3 on 2021-12-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20211231_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_delivery_charge',
            field=models.SmallIntegerField(default=50),
        ),
    ]
