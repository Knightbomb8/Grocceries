# Generated by Django 3.1.7 on 2021-03-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210323_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='inventory',
        ),
        migrations.AddField(
            model_name='vendor',
            name='inventory',
            field=models.ManyToManyField(to='myapp.Item'),
        ),
    ]
