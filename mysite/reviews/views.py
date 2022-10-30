from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    reviews = Reviews.objects.all()
    return render(request, 'reviews/reviews_home.html', {'reviews': reviews})


class NewsDetailView(DetailView):
    model = Reviews
    template_name = 'reviews/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Reviews
    template_name = 'reviews/create.html'

    form_class = ReviewsForm


class NewsDeleteView(DeleteView):
    model = Reviews
    success_url = '/reviews/'
    template_name = 'reviews/reviews_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ReviewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'reviews/create.html', data)
