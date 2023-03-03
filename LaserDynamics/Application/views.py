from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def index(request):
    # send_mail(subject = 'Thank you for signing up!', 
    #           message = 'Someone visited the index page!',
    #           from_email = settings.EMAIL_HOST_USER,
    #           recipient_list=['mhanks445@yahoo.com'],
    #           fail_silently=False,

    #           )

    return render(request, 'Application/index.html')


def userLogin(request):
    if request.method == "POST":
        ...





def redirectTest(request):
    return redirect(reverse('application:index'))