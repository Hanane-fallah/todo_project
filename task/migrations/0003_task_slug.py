# Generated by Django 4.1.5 on 2023-01-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_done_task_title_alter_task_task_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(max_length=20, null=True),
        ),
    ]
