
# Register your models here.
from django.contrib import admin

from .models import Branches, Coast, Timetable

admin.site.register(Branches)
admin.site.register(Coast)
admin.site.register(Timetable)
