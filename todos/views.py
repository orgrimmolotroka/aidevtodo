from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        messages.success(self.request, 'Todo created successfully!')
        return super().form_valid(form)


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        messages.success(self.request, 'Todo updated successfully!')
        return super().form_valid(form)


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Todo deleted successfully!')
        return super().delete(request, *args, **kwargs)


def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    status = "completed" if todo.completed else "marked as incomplete"
    messages.success(request, f'Todo "{todo.title}" {status}!')
    return redirect('todo_list')
