from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.


def home(request):
    context = {
        'title':'Home',
        'all_images': Image.get_all()
    }
    return render(request, 'gallery/index.html', context )
