from django.urls import path

from . import views

app_name = 'application'
urlpatterns = [
    path('', views.index, name='index'),
    path('redirectTest', views.redirectTest, name='redirectTest'),
]