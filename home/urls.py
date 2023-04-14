from django.urls import path
from . import views

"""URL Redireciona para serviços """

urlpatterns = [
    path('home/', views.home, name="home_init"),
]