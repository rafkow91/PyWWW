# Generated by Django 3.2.9 on 2022-01-28 18:31

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_publication_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='portrait',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='books/covers/%Y/%m/%d/'),
        ),
    ]
