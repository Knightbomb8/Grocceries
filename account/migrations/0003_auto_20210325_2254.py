# Generated by Django 3.1.7 on 2021-03-26 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210323_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='order',
        ),
        migrations.RemoveField(
            model_name='account',
            name='shoppingCart',
        ),
    ]