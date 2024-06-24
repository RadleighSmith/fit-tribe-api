from django.urls import path
from .views import GroupEventList, GroupEventDetail

urlpatterns = [
    path('group-events/', GroupEventList.as_view(), name='group-event-list'),
    path(
        'group-events/<int:pk>/',
        GroupEventDetail.as_view(),
        name='group-event-detail'
    ),
]
