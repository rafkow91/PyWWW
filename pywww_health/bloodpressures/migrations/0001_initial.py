# Generated by Django 4.0.2 on 2022-02-26 20:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodPressureMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('systolic_blood_pressure', models.PositiveSmallIntegerField()),
                ('diastolic_blood_pressure', models.PositiveSmallIntegerField()),
                ('measurement_datetime', models.DateTimeField(default=datetime.datetime.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, main.models.CheckAgeMixin),
        ),
    ]
