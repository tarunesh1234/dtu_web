# Generated by Django 2.1.4 on 2019-06-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0004_auto_20190629_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
