from django.urls import path
from . import views

"""URL Redireciona para pagina inicial"""

urlpatterns = [
    path('', views.home, name="home_init"),
]