# Generated by Django 4.0.6 on 2022-08-17 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_rename_user_project_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
