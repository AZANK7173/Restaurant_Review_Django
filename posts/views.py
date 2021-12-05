from django.http import HttpResponse, HttpResponseRedirect
from .temp_data import post_data
from django.shortcuts import render
from django.urls import reverse

def detail_post(request, post_id):
    context = {'post': post_data[post_id - 1]}
    return render(request, 'posts/detail.html', context)

def list_posts(request):
    context = {"post_list": post_data}
    return render(request, 'posts/index.html', context)

def create_post(request):
    if request.method == 'POST':
        post_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('posts:detail', args=(len(post_data), )))
    else:
        return render(request, 'posts/create.html', {})
