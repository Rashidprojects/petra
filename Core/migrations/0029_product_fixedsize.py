# Generated by Django 5.0.7 on 2024-08-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0028_alter_product_door_type_1_alter_product_door_type_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='FixedSize',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
