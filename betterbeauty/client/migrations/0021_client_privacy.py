# Generated by Django 2.1 on 2018-10-12 12:34

import client.types
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0020_auto_20181011_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='privacy',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default=client.types.ClientPrivacy('public'), max_length=16),
        ),
    ]
