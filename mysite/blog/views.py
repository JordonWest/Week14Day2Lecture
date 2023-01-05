from django.shortcuts import render, redirect
import datetime

from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.all()[0]
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'type_of_request': 'New'})

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.all()[0]
            post.published_date = datetime.datetime.now() #post.published_date=post.published_date
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_post(request, blog_id, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post_list')

## COMMENTS BELOW
def new_comment(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'type_of_request': 'New'})

def edit_comment(request, post_id, comment_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form, 'type_of_request': 'New'})

def delete_comment(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('post_detail', post_id=post_id)

