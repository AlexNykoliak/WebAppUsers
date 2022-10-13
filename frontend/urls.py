from django.urls import path

from .views import UserListView, UserDetailView

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('', UserListView.as_view(), name='home')
]

