# Generated by Django 2.2.7 on 2020-09-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0005_auto_20200913_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='util',
            field=models.FloatField(default=0.0),
        ),
    ]
