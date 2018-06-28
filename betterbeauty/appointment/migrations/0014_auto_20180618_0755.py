# Generated by Django 2.0.3 on 2018-06-18 11:55

import appointment.types
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0013_appointmentservice_discount_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentStatusHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'New'), ('cancelled_by_client', 'Cancelled by client'), ('cancelled_by_stylist', 'Cancelled by stylist'), ('no_show', 'No show'), ('checked_out', 'Client checked out')], default=appointment.types.AppointmentStatus('new'), max_length=30)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'appointment_status_history',
            },
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='status_updated_at',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='status_updated_by',
        ),
        migrations.AddField(
            model_name='appointmentstatushistory',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_history', to='appointment.Appointment'),
        ),
        migrations.AddField(
            model_name='appointmentstatushistory',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appointment_updates', to=settings.AUTH_USER_MODEL),
        ),
    ]