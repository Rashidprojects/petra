# Generated by Django 5.0.7 on 2024-07-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0021_material_product_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='Material',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
