# Generated by Django 2.1 on 2019-01-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0030_client_sms_notifications_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]