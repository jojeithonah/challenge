# Generated by Django 3.0.8 on 2020-07-23 21:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200723_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999.8)], verbose_name='Value'),
        ),
    ]