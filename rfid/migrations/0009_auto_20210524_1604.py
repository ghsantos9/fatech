# Generated by Django 3.1.2 on 2021-05-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0008_auto_20210524_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfidlogs',
            name='rfid',
            field=models.CharField(max_length=30),
        ),
    ]
