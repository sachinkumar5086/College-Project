# Generated by Django 5.0.3 on 2024-06-01 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_alter_mylectures_department_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mylectures',
        ),
    ]
