from django.urls import path
from . import views

app_name = 'instructapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('/profile/', views.profile, name='profile'),
    path('/course_page/', views.course_page, name='course_page')
]