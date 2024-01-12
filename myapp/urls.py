from django.urls import path
from . import views

# these are all different url paths
# views contain the function necessary for that path
urlpatterns = [
    path('', views.index, name = 'index'),
    path('counter', views.counter, name = 'counter'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login')
]