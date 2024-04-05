# Generated by Django 4.2.5 on 2024-04-04 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('image', models.ImageField(default='null', upload_to='categories', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Almace',
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=15)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=15)),
                ('lista_precios', models.IntegerField(default=0)),
                ('porcentaje_iva', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('id_Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.almacen')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon', models.CharField(max_length=200)),
                ('rfc', models.CharField(max_length=13)),
                ('credito', models.BooleanField(default=False)),
                ('limite_credito', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('dias_credito', models.IntegerField(default=0)),
                ('lista_precios', models.IntegerField(default=1)),
                ('nombre_comercial', models.CharField(max_length=200, null=True)),
                ('dirEstado', models.CharField(max_length=200, null=True)),
                ('dirCiudad', models.CharField(max_length=200, null=True)),
                ('dirColonia', models.CharField(max_length=200, null=True)),
                ('dircalle', models.CharField(max_length=200, null=True)),
                ('dirnumext', models.CharField(max_length=10)),
                ('dirnumint', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Existencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.article')),
                ('id_almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.almacen')),
            ],
            options={
                'verbose_name': 'Existencia',
                'verbose_name_plural': 'Existencias',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entregado', models.BooleanField(default=True)),
                ('devolucion', models.BooleanField(default=False)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.article')),
                ('cantidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.existencia')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
