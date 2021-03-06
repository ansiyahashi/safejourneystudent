# Generated by Django 3.1.1 on 2021-04-15 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210408_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=50)),
                ('starting_point', models.CharField(max_length=50)),
                ('end_point', models.CharField(max_length=50)),
                ('BUS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.bus')),
            ],
        ),
    ]
