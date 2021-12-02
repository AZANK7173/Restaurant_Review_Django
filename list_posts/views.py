from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'list_posts/index.html', context)

def about(request):
    context = {}
    return render(request, 'list_posts/about.html', context)
