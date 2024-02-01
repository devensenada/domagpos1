# Generated by Django 4.2.5 on 2024-01-17 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('POS', '0002_delete_cliente_delete_producto'),
    ]

    operations = [
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
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('image', models.ImageField(default='null', upload_to='categories', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.article')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='id_Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POS.category'),
        ),
    ]
