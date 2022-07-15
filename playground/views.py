#view function takes a request and returns a response

#Request handler

from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
  return HttpResponse('Hello World')    # -> Map to a URL

