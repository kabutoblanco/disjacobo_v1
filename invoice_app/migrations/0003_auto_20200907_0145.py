# Generated by Django 2.2.7 on 2020-09-07 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0002_auto_20200907_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=models.IntegerField(choices=[(1, 'CONTADO'), (2, 'CREDITO')], default=1),
        ),
    ]