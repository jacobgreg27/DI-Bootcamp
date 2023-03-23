from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_view, name='todo'),
    path('display_todos/', views.display_todos, name='display_todos'),
]
