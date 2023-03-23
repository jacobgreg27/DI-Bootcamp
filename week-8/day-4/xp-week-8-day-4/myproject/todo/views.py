from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def todo_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_todos')
    else:
        form = TodoForm()
    return render(request, 'todo/todo.html', {'form': form})

def display_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/display_todos.html', {'todos': todos})

