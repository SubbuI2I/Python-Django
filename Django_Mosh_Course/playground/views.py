from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x= 1*2
    x= x*x
    return x

def say_hello(request):
    x= calculate()
    context = {
        'x':x
    }
    return render( request, 'hello.html' ,context )