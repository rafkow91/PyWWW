# Generated by Django 3.2.9 on 2022-01-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20220102_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]