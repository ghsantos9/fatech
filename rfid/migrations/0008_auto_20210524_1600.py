# Generated by Django 3.1.2 on 2021-05-24 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0007_rfidusuarios_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfidlogs',
            name='rfid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfid.rfidusuarios'),
        ),
    ]