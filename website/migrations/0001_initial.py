# Generated by Django 3.1.7 on 2021-03-12 14:11

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='les_categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('le_nom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='les_ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('le_nom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='les_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('le_nom', models.CharField(max_length=250, unique=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('sub', models.CharField(blank=True, max_length=250, null=True)),
                ('date_expiration', models.CharField(blank=True, max_length=250, null=True)),
                ('la_photo', models.ImageField(upload_to='image/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('categorie', models.ManyToManyField(to='website.les_categorie')),
                ('villes', models.ManyToManyField(blank=True, null=True, to='website.les_ville')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]