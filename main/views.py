from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about_me(request):
    return render(request, 'main/about-me.html')

def photo_gallery(request):
    return render(request, 'main/photos.html')
