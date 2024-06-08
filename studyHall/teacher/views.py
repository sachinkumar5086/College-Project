from django.shortcuts import render
from django.http import HttpResponse
from student.models import *



# Create your views here.
def index(request):

    return render(request,'teacher/index.html')

def lecturesdepartment(request):
    department_id=request.session['department_id']
    cdata = semester.objects.filter().order_by('id')
    edata=department.objects.filter(id=department_id).order_by('id')
    md={"cdata":cdata,"edata":edata}
    return render(request,'teacher/lecturedepartment.html',md)
def lectures(request):
    department_id=request.session['department_id']
    department=request.session['department']
    semester_id=request.GET.get('semester_id')
    sdata=subject.objects.filter(semester=semester_id,department=department_id)
    cdata = mylectures.objects.filter(semester=semester_id, department=department).order_by('-id')
    if request.method == "POST":
        subject_name=request.POST.get('subject')
        vlink=request.POST.get('link')
        desc=request.POST.get('desc')
        thumbnail=request.FILES['thumbnail']
        date=request.POST.get('date')
        mylectures(subject=subject_name,vlink=vlink,thumbnail=thumbnail,department=department,semester=semester_id,video_description=desc,added_date=date).save()
        return HttpResponse("<script>alert('Lecture is added successfully...');location.href='/teacher/lecturedepartment/'</script>")
    md={"cdata":cdata,"sdata":sdata}
    return render(request,'teacher/lectures.html',md)
def lecturesvideo(request):
    subject_name=request.GET.get('subject_name')
    vdata=mylectures.objects.filter(subject=subject_name).order_by('-id')
    md={"vdata":vdata}
    return render(request,'teacher/lecturesvideo.html',md)
    # department_id = request.session.get('department_id')
    # semester_id = request.GET.get('semester_id')
    # vdata = mylectures.objects.filter(department=department_id,semester=semester_id)
    # md = {"vdata": vdata}
    # return render(request, 'teacher/lecturesvideo.html', md)

def notedepartment(request):
    department_id=request.session.get('department_id')
    semester_id=request.session.get('semester_id')
    cdata = semester.objects.filter().order_by('id')
    edata = department.objects.filter(id=department_id).order_by('id')
    md = {"cdata":cdata,"edata":edata}
    return render(request, 'teacher/notesdepartment.html', md)
def notesubject(request):
    semester=request.GET.get('semester_id')
    department_id=request.session['department_id']
    department_name=department.objects.filter(id=department_id)
    sdata = subject.objects.filter(semester=semester, department=department_id)
    if request.method == "POST":
        subject_name=request.POST.get('subject')
        desc=request.POST.get('desc')
        pdf=request.FILES['note']
        date=request.POST.get('date')
        enotes(subject=subject_name,description=desc,notes_pdf=pdf,added_date=date,department=department_name,semester=semester).save()
        return HttpResponse("<script>alert('E-note is added successfully...');location.href='/teacher/notesubject/'</script>")
    md={"sdata":sdata}
    return render(request,'teacher/notesubject.html',md)
def note(request):
    subject_id=request.GET.get('subject_id')
    department_id=request.session['department_id']
    sdata=subject.objects.filter(id=subject_id)
    ndata = enotes.objects.filter(subject=subject_id,department=department_id).order_by('-id')
    md={"ndata":ndata,"sdata":sdata}
    return render(request,'teacher/notes.html',md)
def library(request):
    return render(request,'teacher/library.html')
def softwarekit(request):
    x=mysoftware.objects.all().order_by('-id')
    if request.method=="POST":
        title=request.POST.get('title')
        link=request.POST.get('link')
        desc=request.POST.get('desc')
        date=request.POST.get('date')
        pic=request.FILES['pic']
        mysoftware(software_title=title,link=link,software_description=desc,software_date=date,software_picture=pic).save()
        return HttpResponse("<script>alert('Software is added successfully...');location.href='/student/softwarekit/'</script>")
    md={"sdata":x}
    return render(request,'teacher/softwarekit.html',md)

def uprofile(request):
    user=request.session.get('user')
    udata=teacher.objects.filter(email=user)
    upd=teacher.objects.get(email=user)
    oldpasswd=request.POST.get('opasswd')
    md={"udata":udata}
    if request.method == "POST":
        if upd.passwd == oldpasswd:
            upd.name = request.POST.get('name')
            upd.save()
            upd.mobile = request.POST.get('mobile')
            upd.save()
            upd.passwd = request.POST.get('passwd')
            upd.save()
            upd.pic = request.FILES['fu']
            upd.save()
            # student(name=name , mobile=number, passwd=passwd, pic=profile)._do_update()
            return HttpResponse(
                "<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")


        else:
            return HttpResponse("<script>alert('wrong password....');location.href='/student/uprofile/'</script>")
            #signup(name=name,mobile=mobile,passwd=passwd,college=college,course=course,profile=picture,email=user).save()
        #return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
    return render(request,'teacher/uprofile.html',md)
def mytask(request):
    user = request.session.get('user')
    department= request.session.get('department_id')
    semester = request.session.get('semester_id')
    x=giventask.objects.filter(department=department,semester=semester)
    data = submittedtask.objects.filter(userid=user)

    md={"tdata":x,"data":data}
    return render(request,'student/tasks.html',md)
# user=request.session.get('user')
#     batchid=request.session.get('batchid')
#     if user:
#         tdata=mytask.objects.filter(taskbatch=batchid)
#         data=submittedtask.objects.filter(userid=user)
#     md={"tdata":tdata,"data":data}
#     return render(request,'student/tasks.html',md)

def stask(request):
    user=request.session.get('user')
    if request.method=="POST":
        tid=request.POST.get('tid')
        subject = request.POST.get('subject')
        answer_file=request.FILES['fu']
        x=submittedtask.objects.filter(taskid=tid,userid=user).count()
        print(x)
        if x==1:
            return HttpResponse("<script>alert('This task is already submitted...');location.href='/teacher/tasks'</script>")
        else:
            submittedtask(subject=subject,taskid=tid,answer_file=answer_file,userid=user).save()
            return  HttpResponse("<script>alert('Your task has been submitted successfully...');location.href='/teacher/tasks'</script>")
    return render(request,'teacher/stask.html')

def myliveclasses(request):
    department_id = request.session.get('department_id')
    semester_id = request.session.get('semester_id')
    data=liveclass.objects.filter(department=department_id,semester=semester_id)
    md={"data":data}
    return render(request,'teacher/liveclasses.html',md)
def MySubject(request):
    department = request.session.get('department_id')
    teacher=request.session['user']
    x=subject.objects.filter(department=department,teacher=teacher)
    md={"sdata":x}
    return render(request,'teacher/subject.html',md)
def myAttendence(request):
    return render(request,'teacher/attendence.html')
def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['userpic']
        del request.session['username']
        return HttpResponse("<script>location.href='/user/index/'</script>")
    return render(request,'teacher/logout.html')