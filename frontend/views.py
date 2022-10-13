from django.views.generic import ListView

from backend.models import User


class UserListView(ListView):
    model = User
    template_name = 'home.html'




