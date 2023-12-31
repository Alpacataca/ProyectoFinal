# Generated by Django 4.2.1 on 2023-07-18 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0003_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Empleado',
        ),
        migrations.RenameModel(
            old_name='Curso',
            new_name='Equipo',
        ),
        migrations.RenameModel(
            old_name='Profesor',
            new_name='Gerente',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
