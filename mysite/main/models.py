from django.db import models


class Branches(models.Model):
    branch = models.CharField('Branch', max_length=50, default='')
    adress = models.CharField('Adress', max_length=250, default='')

    def __str__(self):
        return self.branch

    def get_absolute_url(self):
        return f'/branches/{self.id}'

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Coast(models.Model):
    branch = models.ForeignKey('Branches', on_delete=models.CASCADE)
    type_of_abonem = models.CharField('Type', max_length=50, default='')
    coast = models.IntegerField('Coast')

    def __str__(self):
        return self.type_of_abonem

    def get_absolute_url(self):
        return f'/coasts/{self.id}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Timetable(models.Model):
    branch = models.ForeignKey('Branches', on_delete=models.CASCADE)
    group_name = models.CharField('Group', max_length=50, default='')
    day = models.CharField('Day', max_length=50, default='')
    time = models.TimeField('Time')
    age = models.IntegerField('Age')

    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return f'/timetable/{self.id}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'