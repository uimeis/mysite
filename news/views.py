from django.shortcuts import render
from .models import New

# Create your views here.
def new_page(request):
    news = New.objects
    return render(request, 'news.html', {'news':news})