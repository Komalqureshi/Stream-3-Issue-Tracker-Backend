# Generated by Django 2.1.5 on 2019-02-02 01:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.CharField(blank=True, max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('detail', models.TextField()),
                ('created', models.DateField(default=datetime.date.today)),
                ('_type', models.CharField(choices=[('BUG', 'BUG'), ('FEATURE', 'FEATURE')], default='BUG', max_length=200)),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('REOPEN', 'REOPEN'), ('IN PROGRESS', 'IN PROGRESS'), ('ON HOLD', 'ON HOLD'), ('CLOSED', 'CLOSED')], default='OPEN', max_length=100)),
                ('urgency', models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], default='MEDIUM', max_length=200)),
                ('attempted_solution', models.TextField(blank=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Technician', to='common.Technician')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='issues.Ticket')),
            ],
        ),
    ]