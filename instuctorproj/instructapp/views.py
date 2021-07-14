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

def public_page(request):
    return render(request, 'instructapp/public_page.html/')

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
def profile_management(request):
    user_profile = request.user
    context = {
        'user_profile':user_profile,
    }
    return render(request, 'instructapp/profile_management.html', context)

@login_required
def courses_taught(request):
    user = User.objects.get(id=request.GET['user_id'])
    print(user)
    courses_instructing = Course.objects.filter(instructor=user)
    instructing = []
    for course in courses_instructing:
        instructing.append({
            'title':course.title,
            'id': course.id,
            'start_date': course.start_date,
        })
    return JsonResponse({'instructing':instructing})

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

@login_required
def create_course(request):
    data = json.loads(request.body)
    title = data['title']
    overview = data['overview']
    start_date  = data['start_date']
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    instructor = request.user
    price = data['price']
    course_set = Course(title=title,overview=overview,start_date=start_date,instructor=instructor,price=price)
    course_set.save()
    return HttpResponse('ok')

@login_required
def edit_profile(request):
    data = json.loads(request.body)
    user_set = request.user
    if data['username'] == '':
        user_set.username == user_set.username
    else:
        user_set.username = data['username']
    if data['password'] == '':
        user_set.password = user_set.password
    else:
        user_set.password = data['password']
    
    user_set.save()
    return HttpResponse('ok')