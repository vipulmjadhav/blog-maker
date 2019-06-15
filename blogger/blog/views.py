from django.shortcuts import render
from django.http import HttpResponse

posts = [

    {
        'Author': 'vipul jadhav',
        'title': 'health post',
        'content': 'Drink more water',
        'date': 'jun 15 2019'
    },

    {
        'Author': 'vedant jadhav',
        'title': 'game post',
        'content': 'Game less',
        'date': 'jun 15 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})





