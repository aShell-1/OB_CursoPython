# Generated by Django 3.2.14 on 2022-08-01 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('fecha_nacimiento', models.DateField()),
                ('imagen', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('fecha_estreno', models.DateField()),
                ('duracion', models.TimeField()),
                ('resumen', models.TextField(help_text='de que va la peli', max_length=200)),
                ('imagen', models.URLField()),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='muviapp.director')),
            ],
        ),
    ]
