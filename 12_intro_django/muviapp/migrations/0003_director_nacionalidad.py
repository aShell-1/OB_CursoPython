# Generated by Django 3.2.14 on 2022-08-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muviapp', '0002_auto_20220803_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='nacionalidad',
            field=models.CharField(max_length=20, null=True),
        ),
    ]