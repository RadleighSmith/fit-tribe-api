from django.urls import path
from blog_comments import views

urlpatterns = [
    path('blog-comments/', views.BlogCommentList.as_view()),
    path('blog-comments/<int:pk>/', views.BlogCommentDetail.as_view())
]
