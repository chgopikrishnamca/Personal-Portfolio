from Blog.models import Blog
from django.shortcuts import render

def home(request):
    blogs = Blog.objects.order_by('-date')[:5] # [:5] tells to pick last 5 recent blogs
    return render(request, 'Blog/home.html', {'blogs': blogs})
