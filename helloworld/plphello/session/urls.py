from django.urls import path
from . import views


urlpattern = [
    path('hello/', views.hello, name='hello'),
]