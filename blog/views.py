from django.shortcuts import render
from .models import New

# Create your views here.
def new_page(request):
    return render(request, 'news.html', {'new':new})