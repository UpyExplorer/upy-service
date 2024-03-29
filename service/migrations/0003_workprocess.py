# Generated by Django 4.0 on 2022-01-06 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_workuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('work_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.workstation')),
            ],
            options={
                'verbose_name': 'Work Process',
                'verbose_name_plural': 'Work Process',
                'db_table': 'work_process',
            },
        ),
    ]
