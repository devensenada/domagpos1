# Generated by Django 4.2.5 on 2024-06-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_productos_porc_util_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_familia', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Familia',
                'verbose_name_plural': 'Familias',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_marca', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_unidadmedida', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'UnidadMedida',
                'verbose_name_plural': 'UnidadesMedidas',
            },
        ),
    ]
