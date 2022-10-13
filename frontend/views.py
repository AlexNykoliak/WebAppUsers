from django.views.generic import ListView, DetailView

from backend.models import User


class UserListView(ListView):
    model = User
    template_name = 'home.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


