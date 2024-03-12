from django.contrib import admin
from .models import *
# Register your models here.
class departmentAdmin(admin.ModelAdmin):
    list_display = ('id','department_name')
admin.site.register(department,departmentAdmin)

class semesterAdmin(admin.ModelAdmin):
    list_display = ('id','semester')
admin.site.register(semester,semesterAdmin)

class rolesAdmin(admin.ModelAdmin):
    list_display = ('id','roles')
admin.site.register(roles,rolesAdmin)

class sessionAdmin(admin.ModelAdmin):
    list_display = ('id','session')
admin.site.register(session,sessionAdmin)



class studentAdmin(admin.ModelAdmin):
    list_display = ('student_ID','name','email','admit_year','passwd','mobile','pic','role','department','semester')
admin.site.register(student,studentAdmin)

class contactusAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','mobile','message')
admin.site.register(contactus,contactusAdmin)

class myfeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','message')
admin.site.register(myfeedback,myfeedbackAdmin)

class placementAdmin(admin.ModelAdmin):
    list_display = ('id','student_picture','student_name','session','company_name')
admin.site.register(placement,placementAdmin)

class mylecturesAdmin(admin.ModelAdmin):
    list_display = ('id','subject','department','semester','vlink','thumbnail','video_description','added_date')
admin.site.register(mylectures,mylecturesAdmin)
class enotesAdmin(admin.ModelAdmin):
    list_display = ('id','subject','note_pic','notes_pdf','department','semester','added_date')
admin.site.register(enotes,enotesAdmin)

class giventaskAdmin(admin.ModelAdmin):
    list_display = ('id','department','semester','subject','task_file','added_date')
admin.site.register(giventask,giventaskAdmin)
class  submittedtaskAdmin(admin.ModelAdmin):
    list_display = ('id','subject','answer_file','taskid','userid','marks','submit_date','marks_date')
admin.site.register(submittedtask,submittedtaskAdmin)
class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','slider_pic')
admin.site.register(slider,sliderAdmin)

class teacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_Id','name','email','passwd','department','role','mobile','joining_date','pic','address','salary')
admin.site.register(teacher,teacherAdmin)

class subjectAdmin(admin.ModelAdmin):
    list_display = ('id','subject_code','subject_name','department','semester','teacher','date')
admin.site.register(subject,subjectAdmin)