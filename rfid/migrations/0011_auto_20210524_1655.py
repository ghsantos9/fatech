# Generated by Django 3.1.2 on 2021-05-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0010_auto_20210524_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfidusuarios',
            name='rfid',
        ),
        migrations.AddField(
            model_name='rfidusuarios',
            name='rfid',
            field=models.ManyToManyField(to='rfid.rfidLogs'),
        ),
    ]