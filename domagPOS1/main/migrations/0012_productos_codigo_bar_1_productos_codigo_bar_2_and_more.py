# Generated by Django 4.2.5 on 2024-05-15 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_productos_unidad_inv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='codigo_bar_1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='productos',
            name='codigo_bar_2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='productos',
            name='codigo_bar_3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='productos',
            name='codigo_bar_4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='productos',
            name='codigo_bar_5',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='productos',
            name='codigo_prov',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='productos',
            name='moneda',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='productos',
            name='porc_util_1',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='porc_util_2',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='porc_util_3',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='porc_util_4',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='porc_util_5',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio1',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio2',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio3',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio4',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio5',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=15),
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad_Unidad_Compras',
            field=models.IntegerField(default=1),
        ),
    ]
