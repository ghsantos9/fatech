# Generated by Django 3.1.7 on 2021-05-19 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0002_auto_20210518_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='rfidLog',
            new_name='rfidLogs',
        ),
    ]
