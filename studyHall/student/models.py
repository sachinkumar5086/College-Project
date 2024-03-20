from django.db import models

# Create your models here.

class department(models.Model):
    department_name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.department_name

class semester(models.Model):
    semester=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.semester

class roles(models.Model):
    roles=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.roles


class session(models.Model):
    session=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.session



class student(models.Model):
    student_ID=models.CharField(max_length=15,null=True)
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField(primary_key=True,max_length=200)
    admit_year=models.DateField(null=True)
    passwd=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(null=True)
    pic=models.ImageField(upload_to='static/profie/',null=True)
    role=models.CharField(max_length=100,null=True,default='Student')
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    semester=models.ForeignKey(semester,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class teacher(models.Model):
    teacher_Id=models.CharField(max_length=15,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(primary_key=True,max_length=150)
    passwd=models.CharField(max_length=100,null=True)
    department=models.ForeignKey(department,on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(roles, on_delete=models.CASCADE,null=True)
    mobile=models.IntegerField(null=True)
    joining_date=models.DateField(null=True)
    pic=models.ImageField(upload_to='static/profie/',null=True)
    address=models.TextField(null=True)
    salary=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class subject(models.Model):
    subject_code=models.CharField(max_length=100,null=True)
    subject_name=models.CharField(max_length=200,null=True)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    semester=models.ForeignKey(semester,on_delete=models.CASCADE)
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    date=models.DateField(null=True)
    def __str__(self):
        return self.subject_name

class contactus(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=25,null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return self.name

class myfeedback(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    message=models.TextField(null=True)


class placement(models.Model):
    student_picture=models.ImageField(upload_to='static/placement',null=True)
    student_name=models.CharField(max_length=100,null=True)
    session = models.ForeignKey(session, on_delete=models.CASCADE,null=True)
    company_name=models.CharField(max_length=200,null=True)



class mylectures(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(semester, on_delete=models.CASCADE, null=True)
    vlink = models.CharField(max_length=300, null=True)
    thumbnail = models.ImageField(upload_to='static/video', null=True)
    video_description = models.TextField(null=True)
    added_date = models.DateField(null=True)


class enotes(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=True)
    note_pic = models.ImageField(upload_to='static/enotes', null=True)
    notes_pdf = models.FileField(upload_to='static/pdf', null=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(semester, on_delete=models.CASCADE, null=True)
    added_date = models.DateField(null=True)


class giventask(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(semester, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=True)
    task_file = models.FileField(upload_to='static/task', null=True)
    added_date = models.DateField(null=True)


class submittedtask(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=True)
    answer_file = models.FileField(upload_to='static/submittedtask', null=True)
    taskid = models.CharField(max_length=20, null=True)
    userid = models.CharField(max_length=200, null=True)
    marks = models.CharField(max_length=200, null=True)
    submit_date = models.DateField(null=True)
    marks_date = models.DateField(null=True)


class slider(models.Model):
    slider_pic = models.ImageField(upload_to='static/slider/', null=True)

class signUp(models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=150,null=True)
    mobile=models.IntegerField(null=True)
    course=models.CharField(max_length=100,null=True)