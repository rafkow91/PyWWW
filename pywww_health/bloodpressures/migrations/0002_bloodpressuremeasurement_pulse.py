# Generated by Django 4.0.2 on 2022-07-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodpressures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='pulse',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
