# Generated by Django 5.0.3 on 2024-03-31 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_mysoftware_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='liveclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(null=True)),
                ('date', models.DateTimeField(null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.semester')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.teacher')),
            ],
        ),
    ]
