# Generated by Django 5.0.3 on 2024-05-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_placement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedtask',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
