# Generated by Django 5.0.3 on 2024-06-02 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0024_mylectures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylectures',
            name='thumbnail',
        ),
    ]
