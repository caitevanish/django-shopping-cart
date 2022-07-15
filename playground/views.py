#view function takes a request and returns a response

#Request handler

from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
  #Ex.1
  # return HttpResponse('Hello World')    # -> Map to a URL
  
  #ex.2
  return render(request, 'hello.html', {'name': 'Mosh'} )
  #(function) render: (request: HttpRequest, template_name: str | Sequence[str], context: Mapping[str, Any]
  #Third parameter passes in a dictionary; use variable and value to insert into HTML page
    #<h1>Hello {{ name }}</h1>

  #ex.3
  
