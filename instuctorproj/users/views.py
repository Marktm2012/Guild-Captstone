from django.http.response import HttpResponse
from django.shortcuts import render

def register(request):
    return render(request, ('users/register.html'))
