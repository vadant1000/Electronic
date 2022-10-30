from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('coasts', views.coasts, name='coasts'),
    path('branches', views.branches, name='branches'),
    path('timetable', views.timetable, name='timetable'),
    path('cooperation', views.cooperation, name='cooperation'),
    path('reviews', views.reviews, name='reviews')
]
