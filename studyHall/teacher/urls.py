from django.urls import path
from . import views


urlpatterns=[
    path('index/', views.index),
    path('', views.index),
    path('lecturedepartment/', views.lecturesdepartment),
    path('lectures/',views.lectures),
    path('lecturesvideo/', views.lecturesvideo),
    path('notesdepartment/', views.notedepartment),
    path('notesubject/',views.notesubject),
    path('notes/',views.note),
    path('library/',views.library),
    path('softwarekit/',views.softwarekit),
    path('tasks/',views.mytask),
    path('uprofile/',views.uprofile),
    path('liveclasses/', views.myliveclasses),
    path('stask/',views.stask),
    path('subject/',views.MySubject),
    path('attendence/',views.myAttendence),
    path('logout/', views.logout),
]