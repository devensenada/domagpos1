# Generated by Django 4.2.6 on 2023-12-09 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
