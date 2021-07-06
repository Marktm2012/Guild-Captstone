from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'instructapp/base.html')


def course_page(request):
    return render(request, 'instructapp/course_page.html')

@login_required
def profile(request):
    user_profile = request.user
    courses_taught = User.objects.course.all()
    context = {
        'user_profile':user_profile,
        'courses_taught':courses_taught
    }
    return render(request, 'instructapp/profile.html', context)
