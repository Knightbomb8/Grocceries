# Generated by Django 3.1.7 on 2021-03-22 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_vendor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='id',
            field=models.IntegerField(default=0),
        ),
    ]
