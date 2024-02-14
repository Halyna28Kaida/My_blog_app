from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')


def create(request):
    return render(request, 'myapp/create.html')


def topics(request):
    return render(request, 'myapp/topics.html')
