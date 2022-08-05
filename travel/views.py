from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Jack'
    title = 'Home Page'

    return render(request, 'home.html', {'first_name': name,
                                         'page_title': title})


def about(request):
    word = 'About us'
    title = 'About us'

    return render(request, 'about.html', {'page_name': word,
                                          'page_title': title})
