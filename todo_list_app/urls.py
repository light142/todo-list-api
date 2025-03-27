from django.urls import path
from .views import TodoDetailView, TodoListCreateView

urlpatterns = [
    path("todos/", TodoListCreateView.as_view(), name="todo-list"),
    path(
        "todos/<int:pk>/", TodoDetailView.as_view(), name="todo-detail"
    ),  # GET (retrieve), PUT (update), DELETE
]
