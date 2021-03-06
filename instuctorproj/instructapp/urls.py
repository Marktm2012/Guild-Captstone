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
    path('create_course/', views.create_course, name="create_course"),
    path('profile/<int:user_id>/', views.public_page, name="public_page"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('picture_upload', views.picture_upload, name="picture_upload"),
    path('course_cataloug', views.course_cataloug, name="course_cataloug"),
    path('enroll/', views.enroll, name="enroll"),
    path('delete_course/', views.delete_course, name="delete_course"),
    path('delete_lesson', views.delete_lesson, name="delete_lesson"),
]