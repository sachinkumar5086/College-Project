# Generated by Django 5.0.3 on 2024-06-02 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_subject_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enotes',
            name='note_pic',
        ),
    ]
