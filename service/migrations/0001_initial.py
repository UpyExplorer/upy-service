# Generated by Django 4.0 on 2022-01-06 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=15)),
                ('mac_address', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=25)),
                ('host', models.CharField(max_length=25)),
                ('port', models.IntegerField(default=0, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Work Station',
                'verbose_name_plural': 'Work Station',
                'db_table': 'work_station',
            },
        ),
    ]
