from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):

    return render(request,'student/index.html')

def lectures(request):
    department_id=request.session['department_id']
    semester_id=request.session.get('semester_id')
    cdata=mylectures.objects.filter(semester=semester_id,department=department_id).order_by('-id')
    md={"cdata":cdata}
    return render(request,'student/lectures.html',md)
def lecturesvideo(request):
    department_id=request.session.get('department_id')
    subject_id=request.GET.get('subject_id')
    vdata=mylectures.objects.filter(subject=subject_id,department=department_id)
    md={"vdata":vdata}
    return render(request,'student/lecturesvideo.html',md)
def enote(request):
    department_id=request.session.get('department_id')
    semester_id=request.session.get('semester_id')
    ndata = enotes.objects.filter(department=department_id,semester=semester_id)
    md = {"ndata": ndata}
    return render(request, 'student/notes.html', md)
def library(request):
    return render(request,'student/library.html')
def softwarekit(request):
    x=mysoftware.objects.all().order_by('-id')
    md={"sdata":x}
    return render(request,'student/softwarekit.html',md)
def mytask(request):
    x=giventask.objects.all().order_by('-id')
    md={"tdata":x}
    return render(request,'student/tasks.html',md)
def uprofile(request):
    user=request.session.get('user')
    udata=signup.objects.filter(email=user)
    upd=signup.objects.get(email=user)
    oldpasswd=request.POST.get('opasswd')
    md={"udata":udata}
    if request.method=="POST":
        if upd.passwd == oldpasswd:
            if request.POST.get('name'):
                upd.name = request.POST.get('name')
                upd.save()
                return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
            if request.POST.get('mobile'):
                upd.mobile = request.POST.get('mobile')
                upd.save()
                return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
            if request.POST.get('passwd'):
                upd.passwd = request.POST.get('passwd')
                upd.save()
                return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
            if request.FILES['fu']:
                upd.profile= request.FILES['fu']
                upd.save()
                return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
        else:
            return HttpResponse("<script>alert('wrong password....');location.href='/student/uprofile/'</script>")
            #signup(name=name,mobile=mobile,passwd=passwd,college=college,course=course,profile=picture,email=user).save()
        #return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
    return render(request,'student/uprofile.html',md)
def stask(request):
    user=request.session.get('user')
    if request.method=="POST":
        tid=request.POST.get('tid')
        title = request.POST.get('title')
        answer_file=request.FILES['fu']
        x=submittedtask.objects.filter(tid=tid,userid=user).count()
        if x==1:
            return HttpResponse("<script>alert('This task is already submitted...');location.href='/student/tasks'</script>")
        else:
            submittedtask(title=title,tid=tid,answer_file=answer_file,userid=user).save()
            return  HttpResponse("<script>alert('Your task has been submitted successfully...');location.href='/student/tasks'</script>")
    return render(request,'student/stask.html')
def myliveclasses(request):
    department_id = request.session.get('department_id')
    semester_id = request.session.get('semester_id')
    data=liveclass.objects.filter(department=department_id,semester=semester_id)
    md={"data":data}
    return render(request,'student/liveclasses.html',md)
def stask(request):
    user=request.session.get('user')
    if request.method=="POST":
        tid=request.POST.get('tid')
        title = request.POST.get('title')
        answer_file=request.FILES['fu']
        x=submittedtask.objects.filter(tid=tid,userid=user).count()
        if x==1:
            return HttpResponse("<script>alert('This task is already submitted...');location.href='/student/tasks'</script>")
        else:
            submittedtask(title=title,tid=tid,answer_file=answer_file,userid=user).save()
            return  HttpResponse("<script>alert('Your task has been submitted successfully...');location.href='/student/tasks'</script>")
    return render(request,'student/stask.html')
