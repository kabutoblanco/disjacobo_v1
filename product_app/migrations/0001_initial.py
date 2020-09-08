# Generated by Django 2.2.7 on 2020-09-06 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0002_adviser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('value', models.FloatField(default=0.0)),
                ('is_percentage', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Impuesto',
                'verbose_name_plural': 'Impuestos',
            },
        ),
        migrations.CreateModel(
            name='Metaproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=64)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Category')),
            ],
            options={
                'verbose_name': 'Metaproducto',
                'verbose_name_plural': 'Metaproductos',
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('amount', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Presentacion',
                'verbose_name_plural': 'Presentaciones',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=12, unique=True)),
                ('stock', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=0)),
                ('price_cost', models.FloatField(default=0.0)),
                ('price_sale', models.FloatField(default=0.0)),
                ('is_atomic', models.BooleanField(default=True)),
                ('is_store', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('metaproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Metaproduct')),
                ('presentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Presentation')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Trademark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('abbr', models.CharField(max_length=8)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Product')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Provider')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='providers',
            field=models.ManyToManyField(blank=True, through='product_app.Quote', to='user_app.Provider'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Unit'),
        ),
        migrations.AddField(
            model_name='metaproduct',
            name='presentations',
            field=models.ManyToManyField(through='product_app.Product', to='product_app.Presentation'),
        ),
        migrations.AddField(
            model_name='metaproduct',
            name='trademark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Trademark'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('date_record', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Product')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]
