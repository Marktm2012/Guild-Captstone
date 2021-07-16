from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Course, Lesson, LessonUploads, StudentSubmission
from datetime import datetime
import json

# Create your views here.
@login_required
def index(request):
    return render(request, 'instructapp/base.html')

def course_cataloug(request):
    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    return render(request, 'instructapp/course_cataloug.html', context)

def course_page(request, course_id):
    context = {
        'course_id':course_id,
    }
    return render(request, 'instructapp/course_page.html', context)

def public_page(request, user_id):
    public_profile = User.objects.get(id=user_id)
    context = {
        'public_profile':public_profile
    }
    return render(request, 'instructapp/public_page.html/', context)

def get_course(request):
    course_id = request.GET['course_id']
    course_info = Course.objects.get(id=course_id)
    enrolled = course_info.enrolled.all()
    enrolled_list =[]
    for student in enrolled:
        enrolled_list.append({
            'student_name':student.last_name+', '+student.first_name,
            'student_id':student.id,
        })
    instructor = course_info.instructor.last_name+', '+course_info.instructor.first_name
    lesson_info = Lesson.objects.filter(course=course_info)
    course_data = {
        'title':course_info.title,
        'overview':course_info.overview,
        'start_date':course_info.start_date,
        'instructor': instructor,
        'instructor_id': course_info.instructor.id,
        'price':course_info.price,
    }
    lessons = []
    for lesson in lesson_info:
        lessons.append({
            'title': lesson.title,
            'overview':lesson.overview,
            'due_date':lesson.due_date
        })
    return JsonResponse({'course':course_data, 'lessons':lessons, 'students_enrolled':enrolled_list})

@login_required
def profile_management(request):
    user_profile = request.user
    context = {
        'user_profile':user_profile,
    }
    return render(request, 'instructapp/profile_management.html', context)

@login_required
def picture_upload(request):
    user = request.user
    user.profile_picture = request.FILES['profile_picture']
    user.save()
    return HttpResponseRedirect(reverse('instructapp:profile_management'))

@login_required
def courses_taught(request):
    user = User.objects.get(id=request.GET['user_id'])
    courses_instructing = Course.objects.filter(instructor=user)
    courses_attending = Course.objects.filter(enrolled=user)
    instructing = []
    for course in courses_instructing:
        instructing.append({
            'title':course.title,
            'id': course.id,
            'start_date': course.start_date,
        })
    attending = []
    for course in courses_attending:
        attending.append({
            'title': course.title,
            'id': course.id,
            'start_date': course.start_date,
        })
    return JsonResponse({'instructing':instructing, 'attending':attending})

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
    user_set.bio = data['bio']
    user_set.first_name = data['first_name']
    user_set.last_name = data['last_name']
    user_set.email = data['email']
    user_set.phone_number = data['phone_number']
    user_set.location = data['location']
    user_set.save()
    return HttpResponse('ok')

@login_required
def enroll(request):
    data = json.loads(request.body)
    course = Course.objects.get(id=data['course_id'])
    course.enrolled.add(request.user)
    course.save()
    return HttpResponse('ok')