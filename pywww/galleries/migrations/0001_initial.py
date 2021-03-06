# Generated by Django 3.2.9 on 2022-01-30 11:43

from django.db import migrations, models
import django.db.models.deletion
import galleries.models
import main.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('HIDE', 'hide'), ('PUBLISHED', 'published'), ('NEW', 'new')], default='NEW', max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, main.models.CheckAgeMixin),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('HIDE', 'hide'), ('PUBLISHED', 'published'), ('NEW', 'new')], default='NEW', max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('short_description', models.CharField(blank=True, max_length=300)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=galleries.models.upload_to)),
                ('source', models.CharField(blank=True, max_length=512, null=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleries.gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, main.models.CheckAgeMixin),
        ),
    ]
