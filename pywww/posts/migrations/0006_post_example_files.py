# Generated by Django 3.2.9 on 2021-12-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='example_files',
            field=models.FileField(blank=True, null=True, upload_to='posts/examples/'),
        ),
    ]
