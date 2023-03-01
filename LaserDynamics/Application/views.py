from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'Application/index.html')


def redirectTest(request):
    return redirect(reverse('application:index'))