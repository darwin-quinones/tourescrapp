# Generated by Django 4.0.3 on 2022-05-12 17:17

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
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=50)),
                ('puntaje', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar_recidencia', models.CharField(max_length=60)),
                ('genero', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('identificacion', models.IntegerField()),
                ('tipo_identificacion', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.CharField(max_length=20)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
