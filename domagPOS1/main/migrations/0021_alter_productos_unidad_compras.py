# Generated by Django 4.2.5 on 2024-06-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_familia_id_familia_remove_marca_id_marca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Unidad_Compras',
            field=models.IntegerField(),
        ),
    ]