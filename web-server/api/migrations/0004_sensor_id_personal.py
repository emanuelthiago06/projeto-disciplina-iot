# Generated by Django 4.2.7 on 2023-12-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_sensor_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='id_personal',
            field=models.IntegerField(null=True),
        ),
    ]