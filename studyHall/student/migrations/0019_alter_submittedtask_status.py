# Generated by Django 5.0.3 on 2024-05-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_submittedtask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedtask',
            name='status',
            field=models.CharField(default='Pending', max_length=100, null=True),
        ),
    ]
