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

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"images": images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})