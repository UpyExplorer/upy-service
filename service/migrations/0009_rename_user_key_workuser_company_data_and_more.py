# Generated by Django 4.0 on 2022-01-07 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_rename_key_workuser_user_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workuser',
            old_name='user_key',
            new_name='company_data',
        ),
        migrations.RenameField(
            model_name='workuser',
            old_name='user_name',
            new_name='corporate_name',
        ),
    ]