
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

    ]

    operations = [
        migrations.CreateModel(

            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('ADMIN', 'Admin'), ('RENTER', 'Renter')], max_length=10)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('image', models.ImageField(default='', upload_to='main_app/static/uploads')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),

            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roomType', models.CharField(choices=[('1', 'Sigle Room'), ('2', 'Double Room'), ('3', 'Shared Room'), ('4', 'Studio'), ('5', 'Suite'), ('6', 'Guest House')], default='1', max_length=1)),
                ('image', models.ImageField(default='', upload_to='main_app/static/uploads')),
                ('size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(max_length=250)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=100)),

            ],
        ),
    ]
