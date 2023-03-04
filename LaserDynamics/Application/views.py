from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required






# Create your views here.
def index(request):
    # send_mail(subject = 'Thank you for signing up!', 
    #           message = 'Someone visited the index page!',
    #           from_email = settings.EMAIL_HOST_USER,
    #           recipient_list=['mhanks445@yahoo.com'],
    #           fail_silently=False,

    #           )

    return render(request, 'Application/index.html')



def logoutPage(request):
    logout(request)
    return redirect(reverse('Application:userLogin'))




def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('Application:account'))
        
        else:
            context = {'errorMessage': "Invalid login credentials, please try again!"}
            return render(request, 'Application/login.html', context)
    return render(request,'Application/login.html')


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST['username'],
                                        password = request.POST['password'], 
                                        email = request.POST['email'], 
                                        first_name = request.POST['firstName'], 
                                        last_name = request.POST['lastName'])
        user.save()
        return render(request, 'Application/login.html', {})
    return render(request,'Application/signup.html', {})

@login_required(login_url='Application:userLogin')
def account(request):
    return render(request, "Application/account.html")



def redirectTest(request):
    return redirect(reverse('Application:index'))




def aboutUs(request):
    return render(request,'Application/aboutUs.html')