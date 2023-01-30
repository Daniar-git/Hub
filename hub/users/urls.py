from django.urls import path
from . import views

app_name ='users'

urlpatterns = [
    path('users/',views.Users.as_view(),name='users')
]
