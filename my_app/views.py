from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import Todo

def home(request):
    todo = Todo.objects.all()
    name = 'Sewanta'
    return render(request, 'index.html', {'todo': todo, 'abc': name})

def add_todo(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        new_todo = Todo(title=title, description=description)
        new_todo.save()
        return redirect('/home')
    return render(request, 'add_todo.html')  # Assuming you have a template for adding a todo

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/home')

def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.title = request.POST["title"]
        todo.description = request.POST["description"]
        todo.save()
        return redirect('/home')
    return render(request, 'update_todo.html', {'todo': todo})

def show_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'update_todo.html', {'todo': todo})
