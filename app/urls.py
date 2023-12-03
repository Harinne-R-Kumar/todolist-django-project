from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_todos, name='list_todos'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('todos/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]