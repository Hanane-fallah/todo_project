from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_users, name='all'),
    path('<int:task_id>/', views.task_detail, name='task_detail')
]
