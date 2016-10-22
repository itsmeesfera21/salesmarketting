from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import json
from .models import Post

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


def post_detail(request, slug):
	print slug
	slug=slug.split(".")[0]
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_detail.html', {'post': post})    