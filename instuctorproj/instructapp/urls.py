from django.urls import path
from . import views

app_name = 'instructapp'
urlpatterns = [
    path('', views.index, name='index')
]