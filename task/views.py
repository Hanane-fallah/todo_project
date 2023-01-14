from django.shortcuts import render

from task.models import Task
from users.models import User


# Create your views here.
def all_users(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    context = {
        'users': users,
        'tasks': tasks
    }
    return render(request, 'index.html', context)

