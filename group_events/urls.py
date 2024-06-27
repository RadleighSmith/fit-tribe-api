from django.urls import path
from .views import GroupEventList, GroupEventDetail, JoinEvent, LeaveEvent

urlpatterns = [
    path(
        'group-events/',
        GroupEventList.as_view(),
        name='group-event-list'
    ),
    path(
        'group-events/<int:pk>/',
        GroupEventDetail.as_view(),
        name='group-event-detail'
    ),
    path(
        'group-events/<int:pk>/join/',
        JoinEvent.as_view(),
        name='join-event'
    ),
    path(
        'group-events/<int:pk>/leave/',
        LeaveEvent.as_view(),
        name='leave-event'
    ),
]
