# Generated by Django 4.0 on 2023-11-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customuser_is_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_online',
        ),
        migrations.AddField(
            model_name='customuser',
            name='session_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
