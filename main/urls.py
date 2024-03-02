
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about-me.html', views.about_me, name='about_me'),
]
