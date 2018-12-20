# Generated by Django 2.1 on 2018-12-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0011_auto_20181206_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='forced_channel',
            field=models.CharField(blank=True, choices=[('sms', 'SMS message'), ('push', 'Push Notification')], default=None, max_length=16, null=True, verbose_name='Specifically selected channel for current notification'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=1024),
        ),
    ]
