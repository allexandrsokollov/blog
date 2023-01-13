from .models import User
from django.views.generic import DetailView


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user.html'
    context_object_name = 'user'
