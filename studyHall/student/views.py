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