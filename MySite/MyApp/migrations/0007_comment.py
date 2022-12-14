# Generated by Django 4.0.6 on 2022-08-21 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_account_user'),
        ('MyApp', '0006_alter_project_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.TextField()),
                ('Commenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='register.account')),
                ('Project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MyApp.project')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
