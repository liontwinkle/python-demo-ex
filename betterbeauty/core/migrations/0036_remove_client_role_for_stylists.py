# Generated by Django 2.1 on 2018-10-18 19:07
from django.contrib.gis.db.backends.postgis.schema import PostGISSchemaEditor
from django.db import migrations
from django.db.migrations.state import StateApps

from core.types import UserRole


def forwards(apps: StateApps, schema_editor: PostGISSchemaEditor):
    User = apps.get_model('core', 'User')
    users = User.objects.filter(
        role__contains=[UserRole.STYLIST, UserRole.CLIENT], client__isnull=True)
    users.update(role=[UserRole.STYLIST])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20181018_1218'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse_code=migrations.RunPython.noop)
    ]
