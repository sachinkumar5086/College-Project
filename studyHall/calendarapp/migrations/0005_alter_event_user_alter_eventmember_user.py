# Generated by Django 5.0.3 on 2024-03-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0004_alter_event_id_alter_event_user_alter_eventmember_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventmember',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
