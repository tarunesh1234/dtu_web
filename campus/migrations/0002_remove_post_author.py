# Generated by Django 2.0.7 on 2020-03-18 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
