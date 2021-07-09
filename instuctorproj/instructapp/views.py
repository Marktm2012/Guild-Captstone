from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Course, Lesson, LessonUploads, StudentSubmission
from datetime import datetime
import json

# Create your views here.
def index(request):
    return render(request, 'instructapp/base.html')

def course_page(request, course_id):
    context = {
        'course_id':course_id,
    }
    return render(request, 'instructapp/course_page.html', context)

def get_course(request):
    course_id = request.GET['course_id']
    course_info = Course.objects.get(id=course_id)
    instructor = course_info.instructor.last_name+', '+course_info.instructor.first_name
    lesson_info = Lesson.objects.filter(course=course_info)
    course_data = {
        'title':course_info.title,
        'overview':course_info.overview,
        'start_date':course_info.start_date,
        'instructor': instructor,
        'instructor_username':course_info.instructor.username,
        'price':course_info.price,
    }
    lessons = []
    for lesson in lesson_info:
        lessons.append({
            'title': lesson.title,
            'overview':lesson.overview,
            'due_date':lesson.due_date
        })
    return JsonResponse({'course':course_data, 'lessons':lessons})

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
def create_lesson(request):
    data = json.loads(request.body)
    course = Course.objects.get(id=data['course_id'])
    title = data['title']
    overview = data['overview']
    due_date = data['due_date']
    due_date = datetime.strptime(due_date, '%Y-%m-%dT%H:%M')
    lesson_set = Lesson(course=course, title=title, overview=overview, due_date=due_date)
    lesson_set.save()
    return HttpResponse('ok')