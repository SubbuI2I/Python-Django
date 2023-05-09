from django.urls import path
from . import views

# URL configs
urlpatterns = [
    path('hello', views.say_hello , name='say-hello')
]
