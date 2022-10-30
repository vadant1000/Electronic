# Generated by Django 4.1.2 on 2022-10-27 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='', max_length=50, verbose_name='Group')),
                ('day', models.CharField(default='', max_length=50, verbose_name='Day')),
                ('time', models.TimeField(verbose_name='Time')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branches')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.CreateModel(
            name='Coast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_abonem', models.CharField(default='', max_length=50, verbose_name='Type')),
                ('coast', models.IntegerField(verbose_name='Coast')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branches')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
    ]
