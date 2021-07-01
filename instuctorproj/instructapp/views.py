from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'instructapp/base.html')


@login_required
def profile(request):
    user_profile = request.user
    context = {
        'user_profile':user_profile,
    }
    return render(request, 'instructapp/profile.html', context)
