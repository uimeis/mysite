from django.shortcuts import render
from blog.models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs': blogs})