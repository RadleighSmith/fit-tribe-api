from django.contrib import admin
from .models import Workout, WorkoutItem

admin.site.register(Workout)
admin.site.register(WorkoutItem)