# Generated by Django 4.2.7 on 2023-11-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='size',
            field=models.CharField(max_length=100),
        ),
    ]
