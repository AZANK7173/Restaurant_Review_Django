from django.http import HttpResponse, HttpResponseRedirect
from .temp_data import post_data
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post
from django.views import generic

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)


def list_posts(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)

def create_post(request):
    if request.method == 'POST':
        post_restaurant_name = request.POST['restaurant_name']
        post_eval = request.POST['eval']
        post_content = request.POST['content']
        post_date_of_post = request.POST['date_of_post']
        post_poster_url = request.POST['poster_url']

        post = Post(restaurant_name=post_restaurant_name, eval=post_eval, content=post_content, date_of_post=post_date_of_post, 
            poster_url=post_poster_url)

        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.restaurant_name = request.POST['restaurant_name']
        post.eval = request.POST['eval']
        post.content = request.POST['content']
        post.date_of_post = request.POST['date_of_post']
        post.poster_url = request.POST['poster_url']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'posts/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)

class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
