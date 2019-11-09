from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.


def home(request):
    print(request)
    context = {
        'title':'Home',
        'images': Image.get_all()
    }
    return render(request, 'gallery/index.html', context )

def filter_by_category(request,category):
    context = {
        'images':Image.filter_by_category(category)
    }
    return render(request, 'gallery/index.html', context)
