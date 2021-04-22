# Generated by Django 3.1.1 on 2021-04-07 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
    ]
