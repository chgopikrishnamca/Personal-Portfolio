from django.http import request
from Blog.models import Blog
from django.shortcuts import render, get_object_or_404

def blog_home(request):
    blogs = Blog.objects.order_by('-date')[:5] # [:5] tells to pick last 5 recent blogs
    return render(request, 'Blog/blog_home.html', {'blogs': blogs})

def blog_details(request, blog_id):   
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'Blog/blog_details.html', {'blog':blog})