# Generated by Django 4.2.5 on 2024-04-04 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_productos_porc_gastosvarios_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Unidad_Inv',
            field=models.CharField(max_length=200),
        ),
    ]
