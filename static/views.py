from django.shortcuts import render, httpResponse

# Create your views here.
def say_hello(request):
    return httpResponse("hello")