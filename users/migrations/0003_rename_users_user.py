# Generated by Django 4.1.5 on 2023-01-14 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_done_task_title_alter_task_task_type'),
        ('users', '0002_alter_users_profile_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
