from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Course, Lesson, LessonUploads, StudentSubmission
from datetime import datetime

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
        course = Course.objects.get(id=course_id)
        title = request.POST['l_title']
        overview = request.POST['l_overview']
        due_date = request.POST['l_due_date']
        due_date = datetime.strptime(due_date, '%Y-%m-%dT%H:%M')
        lesson_set = Lesson(course=course, title=title, overview=overview, due_date=due_date)
        lesson_set.save()
    return HttpResponseRedirect(reverse('instructapp:course_page', args=(course_id,)))