# Generated by Django 5.0.3 on 2024-03-12 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_teacher_joining_date_teacher_passwd_teacher_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='role',
            field=models.CharField(default='Student', max_length=100, null=True),
        ),
    ]
