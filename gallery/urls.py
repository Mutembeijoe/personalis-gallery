from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name="gallery-home"),
    path('categories/<category>/', views.filter_by_category, name="gallery-category")
]