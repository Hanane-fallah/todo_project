# Generated by Django 4.1.5 on 2023-01-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(default='Screenshot_from_2023-01-07_20-45-18.png', upload_to='images'),
        ),
    ]
