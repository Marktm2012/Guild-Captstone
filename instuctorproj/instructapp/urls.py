from django.urls import path
from . import views

app_name = 'instructapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('<int:course_id>/course_page/', views.course_page, name='course_page'),
    path('<int:course_id>/create_lesson/', views.create_lesson, name="create_lesson")
]