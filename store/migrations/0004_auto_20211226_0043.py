# Generated by Django 3.0.3 on 2021-12-26 00:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211225_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.SmallIntegerField(default=10),
        ),
    ]
