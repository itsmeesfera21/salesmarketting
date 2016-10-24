from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect
import json
from django.template.defaultfilters import slugify
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print posts
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_all(request):
    posts = Post.objects.all()
    print posts
    postss=[]
    for post in posts:
    	postss.append({"title":post.title,"author":post.author_id})
    return HttpResponse(str(postss))
    #return render(request, 'blog/post_list.html', {'posts': posts})    

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print request.POST
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            print  request.user
            #post.published_date = timezone.now()
            #post.slug='%s'%(slugify(request.POST))
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
	posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request,'blog/post_draft_list.html',{'posts':posts})

def post_publish(request,slug):
	post=get_object_or_404(Post,slug=slug)
	post.publish()
	return redirect('post_detail', slug=post.slug)

def post_delete(request,slug):
	post=get_object_or_404(Post,slug=slug)
	post.delete()
	return redirect('post_list')

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, slug):
	print slug
	slug=slug.split(".")[0]
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_detail.html', {'post': post})    