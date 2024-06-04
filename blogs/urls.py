from django.urls import path
from blogs import views

urlpatterns = [
    path('blogs/', views.BlogList.as_view()),
]