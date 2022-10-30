from .models import Reviews
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Превью отзывы'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзывы'
            }),

        }