from django.shortcuts import render
from django.views.generic.list import ListView
from .models import User

class Users(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'


