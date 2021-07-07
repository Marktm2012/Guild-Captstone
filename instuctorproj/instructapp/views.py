from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Course, Lesson, LessonUploads, StudentSubmission

# Create your views here.
def index(request):
    return render(request, 'instructapp/base.html')


def course_page(request, course_id):
    course_info = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course_info)
    context = {
        'course': course_info,
        'lessons': lessons,
    }
    return render(request, 'instructapp/course_page.html', context)

@login_required
def profile(request):
    user_profile = request.user
    courses_taught = Course.objects.filter(instructor=request.user.id)
    context = {
        'user_profile':user_profile,
        'courses_taught':courses_taught
    }
    return render(request, 'instructapp/profile.html', context)

@login_required
def create_lesson(request, course_id):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'instructapp/course_page.html')