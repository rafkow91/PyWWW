# Generated by Django 3.2.9 on 2022-01-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20211204_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/%Y/%m/%d/'),
        ),
    ]
