from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Jack'

    return render(request, 'home.html', {'first_name': name})
