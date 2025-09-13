from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.task_list,name = 'task_list'),
    path('create/', views.task_create, name = 'task_create'),
    path('<int:task_id>/', views.task_create, name = 'task_detail'),
    path('delete<int:task_id>/', views.task_create, name = 'task_delete'),
    path('<int:task_id>/task_completed', views.task_create, name = 'task_completed'),
    path('create/', views.task_create, name = 'task_create'),
]