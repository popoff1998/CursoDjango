# Generated by Django 2.2.5 on 2019-10-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20191008_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='slug',
            field=models.SlugField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=120),
        ),
    ]