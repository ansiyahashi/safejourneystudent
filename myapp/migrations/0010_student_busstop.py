# Generated by Django 3.2 on 2021-04-18 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210418_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='BUSSTOP',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.bus_stop'),
        ),
    ]
