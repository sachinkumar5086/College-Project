# Generated by Django 5.0.3 on 2024-06-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_alter_submittedtask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylectures',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mylectures',
            name='semester',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mylectures',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]