# Generated by Django 5.0.3 on 2024-03-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_contactus_myfeedback_slider_enotes_giventask_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
