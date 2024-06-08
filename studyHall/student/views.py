from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):

    return render(request,'student/index.html')
def lectures(request):
    department_id=request.session['department_id']
    department=request.session['department']
    semester_id=request.session['semester_id']
    sdata=subject.objects.filter(semester=semester_id,department=department_id)
    cdata = mylectures.objects.filter(semester=semester_id,department=department).order_by('-id')
    md={"cdata":cdata,"sdata":sdata}
    return render(request,'student/lectures.html',md)
def lecturesvideo(request):
    subject_name=request.GET.get('subject_name')
    vdata=mylectures.objects.filter(subject=subject_name).order_by('-id')
    md={"vdata":vdata}
    return render(request,'student/lecturesvideo.html',md)

def notesubject(request):
    semester=request.session['semester_id']
    department_id=request.session['department_id']
    department_name=department.objects.filter(id=department_id)
    sdata = subject.objects.filter(semester=semester,department=department_id)
    md={"sdata":sdata}
    return render(request,'student/notesubject.html',md)
def note(request):
    subject_id=request.GET.get('subject_id')
    semester=request.session['semester_id']
    department_id=request.session['department_id']
    sdata=subject.objects.filter(id=subject_id).order_by('-id')
    ndata = enotes.objects.filter(subject=subject_id,department=department_id).order_by('-id')
    md={"ndata":ndata,"sdata":sdata}
    return render(request,'student/notes.html',md)
def library(request):
    return render(request,'student/library.html')
def softwarekit(request):
    x=mysoftware.objects.all().order_by('-id')
    md={"sdata":x}
    return render(request,'student/softwarekit.html',md)


def uprofile(request):
    user=request.session.get('user')
    udata=student.objects.filter(email=user)
    upd=student.objects.get(email=user)
    oldpasswd=request.POST.get('opasswd')
    md={"udata":udata}
    if request.method=="POST":
        if upd.passwd == oldpasswd:
            upd.name=request.POST.get('name')
            upd.save()
            upd.mobile=request.POST.get('mobile')
            upd.save()
            upd.passwd=request.POST.get('passwd')
            upd.save()
            upd.pic=request.FILES['fu']
            upd.save()
            # student(name=name , mobile=number, passwd=passwd, pic=profile)._do_update()
            return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")


        else:
            return HttpResponse("<script>alert('wrong password....');location.href='/student/uprofile/'</script>")

        # if upd.passwd == oldpasswd:
        #     if request.POST.get('name'):
        #
        #         upd.name = request.POST.get('name')
        #         upd.save()
        #         return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
        #     if request.POST.get('mobile'):
        #         upd.mobile = request.POST.get('mobile')
        #         upd.save()
        #         return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
        #     if request.POST.get('passwd'):
        #         upd.passwd = request.POST.get('passwd')
        #         upd.save()
        #         return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
        #     if request.FILES['fu']:
        #         upd.profile= request.FILES['fu']
        #         upd.save()
        #         return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
        # else:
        #     return HttpResponse("<script>alert('wrong password....');location.href='/student/uprofile/'</script>")
            #signup(name=name,mobile=mobile,passwd=passwd,college=college,course=course,profile=picture,email=user).save()
        #return HttpResponse("<script>alert('Your profile is updated successfully...');location.href='/student/uprofile/'</script>")
    return render(request,'student/uprofile.html',md)

def myliveclasses(request):
    department_id = request.session.get('department_id')
    semester_id = request.session.get('semester_id')
    data=liveclass.objects.filter(department=department_id,semester=semester_id)
    md={"data":data}
    return render(request,'student/liveclasses.html',md)

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
    user=request.session.get('student_ID')
    if request.method=="POST":
        tid=request.POST.get('tid')
        subject = request.POST.get('subject')
        answer_file=request.FILES['fu']
        x=submittedtask.objects.filter(taskid=tid,userid=user).count()
        if x==1:
            y = giventask.objects.filter(id=tid)
            print(y)
            y.status = request.POST.get('status')

            return HttpResponse("<script>alert('This task is already submitted...');location.href='/student/tasks'</script>")
        else:
            y=giventask.objects.filter(id=tid)
            y.status=request.POST.get('status')
            submittedtask(subject=subject,taskid=tid,answer_file=answer_file,userid=user).save()
            return  HttpResponse("<script>alert('Your task has been submitted successfully...');location.href='/student/tasks'</script>")
    return render(request,'student/stask.html')

def MySubject(request):
    department = request.session.get('department_id')
    semester = request.session.get('semester_id')
    x=subject.objects.filter(department=department,semester=semester)
    md={"sdata":x}
    return render(request,'student/subject.html',md)

def MyAttendance(request):
    return render(request,'student/attendance.html')
def addmissionForm(request):
    return render(request,'student/addmission.html')
def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['userpic']
        del request.session['username']
        return HttpResponse("<script>location.href='/user/index/'</script>")
    return render(request,'student/logout.html')
