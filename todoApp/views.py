from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import todoModel

# Create your views here.
class TodoList(ListView):
    model = todoModel
    template_name = 'list.html'
    
class TodoDetail(DetailView):
    model = todoModel
    template_name = 'detail.html'
    
class TodoCreate(CreateView):
    model = todoModel
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('list')
    
class TodoDelete(DeleteView):
    model = todoModel
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
    
class TodoUpdate(UpdateView):
    model = todoModel
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')
    