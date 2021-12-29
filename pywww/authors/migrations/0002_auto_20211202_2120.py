# Generated by Django 3.2.9 on 2021-12-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='death_city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
