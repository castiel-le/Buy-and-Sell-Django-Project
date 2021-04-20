from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Kirill',
        'title': 'First item',
        'content': 'Used chair, good state',
        'date_posted':  'April 19, 2021'
    },
    {
        'author': 'John',
        'title': 'Second item',
        'content': 'Carpet, nice',
        'date_posted':  'April 20, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
