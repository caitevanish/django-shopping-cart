from django.urls import path
from . import views

#URLConfig
urlpatterns = [
  path('hello/', views.say_hello)
  #path(route: str, view: (...) -> HttpResponseBase, kwargs: Dict[str, Any] = ..., name: str = ...) -> URLPattern

  #route: playground/hello **took out the 'playground' because it was added in the storefront.urls
    #always add a forward slash after
  #view: views.say_hello

  
]