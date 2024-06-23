from django.urls import path
from .views import FeedList

urlpatterns = [
    path('feed/', FeedList.as_view(), name='feed'),
]
