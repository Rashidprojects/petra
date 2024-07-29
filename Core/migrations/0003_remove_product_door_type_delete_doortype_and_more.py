# Generated by Django 5.0.7 on 2024-07-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_colorshade_doortype_hangingposition_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Door_type',
        ),
        migrations.DeleteModel(
            name='DoorType',
        ),
        migrations.AddField(
            model_name='product',
            name='Door_type',
            field=models.CharField(choices=[('luxury', 'Luxury'), ('single', 'Single'), ('double', 'Double')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
