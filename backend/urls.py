from django.urls import path
from .views import UserView, UserDetail

urlpatterns = [
    path('<int:pk>/', UserView.as_view()),
    path('', UserView.as_view()),
]


