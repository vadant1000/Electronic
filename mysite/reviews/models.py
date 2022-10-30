from django.db import models


class Reviews(models.Model):
    title = models.CharField('Name', max_length=50, default='')
    anons = models.CharField('Anons', max_length=250, default='')
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date of public')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/reviews/{self.id}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


