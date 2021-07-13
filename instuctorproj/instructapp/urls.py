from django.urls import path
from . import views

app_name = 'instructapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile_management/', views.profile_management, name='profile_management'),
    path('course_page/<int:course_id>/', views.course_page, name='course_page'),
    path('create_lesson/', views.create_lesson, name="create_lesson"),
    path('get_course/', views.get_course, name="get_course"),
    path('courses_taught/', views.courses_taught, name="courses_taught"),
    path('create_course/', views.create_course, name="create_course")
]