from django.urls import path
from .views import GroupList, GroupDetail, JoinGroup, LeaveGroup, MembershipList

urlpatterns = [
    path('groups/', GroupList.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),
    path('groups/<int:pk>/join/', JoinGroup.as_view(), name='group-join'),
    path('groups/<int:pk>/leave/', LeaveGroup.as_view(), name='group-leave'),
    path('memberships/', MembershipList.as_view(), name='membership-list'),
]
