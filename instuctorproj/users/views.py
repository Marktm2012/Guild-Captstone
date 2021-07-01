from django.http.response import HttpResponse
from django.shortcuts import render
from .models import User
from datetime import datetime

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

 