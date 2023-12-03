from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'myapp/list_todos.html', {'todos': todos})

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Todo.objects.create(title=title, description=description)
        return redirect('list_todos')
    return render(request, 'myapp/add_todo.html', {})

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo.title = title
        todo.description = description
        todo.save()
        return redirect('list_todos')

    return render(request, 'myapp/edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('list_todos')