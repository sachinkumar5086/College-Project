from django.shortcuts import render
from django.http import HttpResponse
from student.models import *


# Create your views here.
def index(request):
    slider_active=slider.objects.all().order_by('-id')[0]
    slider_pic=slider.objects.all().order_by('-id')[1:]
    mydict={"sactive":slider_active,"sdata":slider_pic}
    return render(request,'user/index.html',mydict)

def about(request):
    return render(request,"user/about.html")
def feedback(request):
    return render(request,'user/feedback.html')
def contact(request):
    course=department.objects.all().order_by('id')
    cdata={"course":course}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('course')
        signUp(name=a,email=b,mobile=c,course=d).save()
    return render(request,'user/contact.html',cdata)


def feedback(request):
    if request.method=="POST":
        a=request.POST.get('fname')
        b=request.POST.get('femail')
        c=request.POST.get('fmsg')
        # d=request.FILES['fp']
        myfeedback(name=a,email=b,message=c).save()
        return HttpResponse("<script>alert('Thanks for giving me feedback'); location.href='/user/feedback/'</script>")
    return render(request,"user/feedback.html")

def studentlogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd = request.POST.get('passwd')
        x=student.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=student.objects.filter(email=email,passwd=passwd)
            request.session['userpic']=str(y[0].pic)
            request.session['username'] = str(y[0].name)
            request.session['department'] = str(y[0].department)
            request.session['department_id'] = str(y[0].department.id)
            request.session['semester'] = str(y[0].semester)
            request.session['semester_id'] = str(y[0].semester.id)

            return HttpResponse("<script>location.href='/student/index/'</script>")
        else:
            return HttpResponse("<script>alert('your username or password is incorrect...');location.href='/user/studentlogin/'</script>")
    return render(request,'user/studentlogin.html')
def successstory(request):
    return render(request,'user/successstory.html')

def teacherlogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd = request.POST.get('passwd')
        x=teacher.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=teacher.objects.filter(email=email,passwd=passwd)
            request.session['userpic']=str(y[0].pic)
            request.session['username'] = str(y[0].name)
            request.session['department'] = str(y[0].department)
            request.session['department_id'] = str(y[0].department.id)
            
            return HttpResponse("<script>location.href='/teacher/index/'</script>")
        else:
            return HttpResponse("<script>alert('your username or password is incorrect...');location.href='/user/teacherlogin/'</script>")
    return render(request,'user/teacherlogin.html')

