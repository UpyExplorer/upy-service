# Generated by Django 4.0 on 2022-01-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_workprocess_work_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workuser',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
