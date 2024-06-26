from django.urls import path
from . import views


urlpatterns=[
    path('index/', views.index),
    path('', views.index),
    path('lectures/', views.lectures),
    path('lecturesvideo/',views.lecturesvideo),
    path('notesubject/',views.notesubject),
    path('notes/',views.note),
    path('library/',views.library),
    path('softwarekit/',views.softwarekit),
    path('tasks/',views.mytask),
    path('uprofile/',views.uprofile),
    path('liveclasses/', views.myliveclasses),
    path('stask/',views.stask),
    path('subject/', views.MySubject),
    path('attendance/', views.MyAttendance),
    path('addmission/', views.addmissionForm),
    path('logout/', views.logout),


]