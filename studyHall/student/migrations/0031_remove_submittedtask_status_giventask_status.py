# Generated by Django 5.0.3 on 2024-06-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0030_alter_enotes_department_alter_enotes_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submittedtask',
            name='status',
        ),
        migrations.AddField(
            model_name='giventask',
            name='status',
            field=models.CharField(default='Pending', max_length=100, null=True),
        ),
    ]
