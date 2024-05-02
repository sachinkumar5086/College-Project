from django.urls import path
from . import views


urlpatterns=[
    path('index/', views.index),
    path('', views.index),
    path('lecturedepartment/', views.lectures),
    path('lectures/',views.lecturesvideo),
    path('notes/',views.enote),
    path('library/',views.library),
    path('softwarekit/',views.softwarekit),
    path('tasks/',views.mytask),
    path('uprofile/',views.uprofile),
    path('liveclasses/', views.myliveclasses),
    path('stask/',views.stask),
]