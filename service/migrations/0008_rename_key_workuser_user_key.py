# Generated by Django 4.0 on 2022-01-07 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_workuser_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workuser',
            old_name='key',
            new_name='user_key',
        ),
    ]