# Generated by Django 3.0.3 on 2021-12-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_popularity_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ordered_quantity',
            field=models.IntegerField(null=True),
        ),
    ]
