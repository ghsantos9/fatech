# Generated by Django 3.1.2 on 2021-05-24 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0011_auto_20210524_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfidusuarios',
            name='rfid',
        ),
        migrations.AddField(
            model_name='rfidusuarios',
            name='rfid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rfid.rfidlogs'),
            preserve_default=False,
        ),
    ]
