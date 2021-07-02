from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import User
from datetime import datetime
import django.contrib.auth
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        if 'is_instructor' in request.POST:
            is_instructor = True
        else:
            is_instructor = False
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        birthday = request.POST['birthday']
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        bio = request.POST['bio']
        print(request.POST['bio'])
        # ----------------------------------
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_instructor = is_instructor
        user.phone_number = phone_number
        user.birthday = birthday
        user.location = location
        user.bio = bio
        user.save()
    return render(request, ('users/register.html'))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username + ' ' + password)
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('instructapp:profile'))
        else:
            return render(request, 'users/register.html', {'error': 'Incorrect username or password'})
    else:
        return render(request, ('users/register.html'))

@login_required
def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('users:register'))