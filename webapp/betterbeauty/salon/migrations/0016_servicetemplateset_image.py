# Generated by Django 2.0.3 on 2018-04-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0015_auto_20180425_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetemplateset',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='template_set_images'),
        ),
    ]
