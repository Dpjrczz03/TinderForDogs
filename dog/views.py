from django.shortcuts import render


def index(request):
    return render(request, 'dog/home.html')
def home(request):
    return render(request, 'dog/home.html')

