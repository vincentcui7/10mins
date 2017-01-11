# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 08:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0003_auto_20161105_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=55, upload_to='', width_field=80)),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
                ('belong_to', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('sex', models.CharField(blank=True, choices=[('性别', '性别'), ('男', '男'), ('女', '女')], max_length=10, null=True)),
                ('password', models.CharField(blank=True, max_length=15, null=True)),
                ('cover', models.FileField(null=True, upload_to='cover_image')),
                ('avatar', models.ImageField(default='static/images/default.png', upload_to='')),
                ('belong_to', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('normal', 'normal'), ('dislike', 'dislike')], max_length=10),
        ),
    ]
