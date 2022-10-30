from django.shortcuts import render
from .models import Branches, Coast, Timetable


# Create your views here.
def index(request):
    data = {
        'title': 'Главная',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def courses(request):
    return render(request, 'main/courses.html')


def coasts(request):
    coast = Coast.objects.all()
    return render(request, 'main/coasts.html', {'coast': coast})


def branches(request):
    branch = Branches.objects.all()
    return render(request, 'main/branches.html', {'branch': branch})


def timetable(request):
    timetable = Timetable.objects.all()
    return render(request, 'main/timetable.html', {'timetable': timetable})


def cooperation(request):
    return render(request, 'main/cooperation.html')


def reviews(request):
    return render(request, 'main/reviews.html')
