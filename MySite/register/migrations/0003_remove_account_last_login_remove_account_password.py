# Generated by Django 4.0.6 on 2022-08-17 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
    ]
