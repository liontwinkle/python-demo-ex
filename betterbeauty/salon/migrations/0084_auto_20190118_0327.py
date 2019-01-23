# Generated by Django 2.1 on 2019-01-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0083_auto_20190114_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylist',
            name='card_fee',
            field=models.DecimalField(decimal_places=2, default=0.0275, max_digits=6),
        ),
        migrations.AddField(
            model_name='stylist',
            name='tax_rate',
            field=models.DecimalField(decimal_places=2, default=0.045, max_digits=6),
        ),
    ]