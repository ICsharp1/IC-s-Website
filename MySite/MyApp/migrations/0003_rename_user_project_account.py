# Generated by Django 4.0.6 on 2022-08-17 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_project_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='account',
        ),
    ]
