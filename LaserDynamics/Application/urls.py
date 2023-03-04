from django.urls import path

from . import views

app_name = 'Application'
urlpatterns = [
    path('', views.index, name='index'),
    path('redirectTest/', views.redirectTest, name='redirectTest'),
    path('userLogin/', views.userLogin, name="userLogin"),
    path('signup/', views.signup, name='signup'),
    path('account/',views.account, name='account'),
]