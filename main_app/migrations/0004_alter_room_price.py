# Generated by Django 4.2.7 on 2023-11-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_room_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]