from django.urls import path
from . import views
urlpatterns = [
    path('', views.news_home, name='reviews_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='reviews-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='reviews-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='reviews-delete')

]

