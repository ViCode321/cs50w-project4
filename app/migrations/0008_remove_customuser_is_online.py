# Generated by Django 4.0 on 2023-11-30 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_customuser_is_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_online',
        ),
    ]
