# Generated by Django 5.0.3 on 2024-03-12 04:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_teacher_roles_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=25, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='myfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_pic', models.ImageField(null=True, upload_to='static/slider/')),
            ],
        ),
        migrations.CreateModel(
            name='enotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_pic', models.ImageField(null=True, upload_to='static/enotes')),
                ('notes_pdf', models.FileField(null=True, upload_to='static/pdf')),
                ('added_date', models.DateField(null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.semester')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.subject')),
            ],
        ),
        migrations.CreateModel(
            name='giventask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_file', models.FileField(null=True, upload_to='static/task')),
                ('added_date', models.DateField(null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.semester')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.subject')),
            ],
        ),
        migrations.CreateModel(
            name='mylectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlink', models.CharField(max_length=300, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='static/video')),
                ('video_description', models.TextField(null=True)),
                ('added_date', models.DateField(null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.semester')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.subject')),
            ],
        ),
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_picture', models.ImageField(null=True, upload_to='static/placement')),
                ('student_name', models.CharField(max_length=100, null=True)),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.session')),
            ],
        ),
        migrations.CreateModel(
            name='submittedtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_file', models.FileField(null=True, upload_to='static/submittedtask')),
                ('taskid', models.CharField(max_length=20, null=True)),
                ('userid', models.CharField(max_length=200, null=True)),
                ('marks', models.CharField(max_length=200, null=True)),
                ('submit_date', models.DateField(null=True)),
                ('marks_date', models.DateField(null=True)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.subject')),
            ],
        ),
    ]
