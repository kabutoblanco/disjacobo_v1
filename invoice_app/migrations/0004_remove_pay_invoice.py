# Generated by Django 2.2.7 on 2020-09-07 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0003_auto_20200907_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='invoice',
        ),
    ]
