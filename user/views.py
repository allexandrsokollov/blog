from django.shortcuts import render
from .models import User


def view_all_users(request):
    users = User.objects.all()
    return render(request, 'user/allUsersTemp.html', {'users': users})
