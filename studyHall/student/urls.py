from django.urls import path
from . import views


urlpatterns=[
    path('index/', views.index),
    path('', views.index),
    path('lectures/', views.lectures),
    path('lecturesvideo/',views.lecturesvideo),
    path('notes/',views.enote),

]