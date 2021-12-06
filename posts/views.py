from django.http import HttpResponse, HttpResponseRedirect
from .temp_data import post_data
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post, Review
from .forms import PostForm, ReviewForm
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
        form = PostForm(request.POST)
        if form.is_valid():
            post_restaurant_name = form.cleaned_data['restaurant_name']
            post_eval = form.cleaned_data['eval']
            post_content = form.cleaned_data['content']
            post_date_of_post = form.cleaned_data['date_of_post']
            post_poster_url = form.cleaned_data['poster_url']

            post = Post(restaurant_name=post_restaurant_name, eval=post_eval, content=post_content, date_of_post=post_date_of_post, 
            poster_url=post_poster_url)

            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/create.html', context)

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.restaurant_name = form.cleaned_data['restaurant_name']
            post.eval = form.cleaned_data['eval']
            post.content = form.cleaned_data['content']
            post.date_of_post = form.cleaned_data['date_of_post']
            post.poster_url = form.cleaned_data['poster_url']
            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'restaurant_name': post.restaurant_name,
                'eval': post.eval,
                'content': post.content,
                'date_of_post': post.date_of_post,
                'poster_url': post.poster_url
            })

    context = {'post': post, 'form': form}
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


def create_review(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            post=post)
            review.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/review.html', context)
