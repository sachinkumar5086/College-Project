from django.urls import path
from . import views

urlpatterns=[

    path('', views.index),
    path('index/', views.index),
    path('about/', views.about),
    path('feedback/', views.feedback),
    path('login/', views.login),
    path('contact/', views.contact),
    path('successstory/', views.successstory),
    path('teacherlogin/',views.teacherlogin),


]
