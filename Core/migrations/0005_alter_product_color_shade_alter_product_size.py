# Generated by Django 5.0.7 on 2024-07-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_product_color_shade_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Color_shade',
            field=models.ManyToManyField(blank=True, to='Core.colorshade'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Size',
            field=models.ManyToManyField(blank=True, to='Core.size'),
        ),
    ]
