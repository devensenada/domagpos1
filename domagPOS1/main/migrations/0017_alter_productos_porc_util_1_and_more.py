# Generated by Django 4.2.5 on 2024-06-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_productos_t_cambio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='porc_util_1',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
        migrations.AlterField(
            model_name='productos',
            name='porc_util_2',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
        migrations.AlterField(
            model_name='productos',
            name='porc_util_3',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
        migrations.AlterField(
            model_name='productos',
            name='porc_util_4',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
        migrations.AlterField(
            model_name='productos',
            name='porc_util_5',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
        migrations.AlterField(
            model_name='productos',
            name='t_cambio',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
    ]
