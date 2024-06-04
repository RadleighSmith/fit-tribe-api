from django.urls import path
from blog_likes import views

urlpatterns = [
    path('blog-likes/', views.BlogLikeList.as_view()),
    path('blog-likes/<int:pk>/', views.BlogLikeDetail.as_view()),
]