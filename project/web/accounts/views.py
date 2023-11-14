from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
import re




# Create your views here.

def signin(request):
    if request.method == 'POST' and 'btnin' in request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
        else:
            messages.error(request, 'username or password invalid')
    return render(request, 'accounts/signin.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')


 

def signup(request):
    if request.method == 'POST' and 'btnup' in request.POST:
        #variables for fields
        email = None
        username = None
        password = None

        is_added = None

        #Get values from the form
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'error in email ')
        if 'user' in request.POST:
            username = request.POST['user']
        else:
            messages.error(request, 'error in username ')
        if 'pass' in request.POST:
            password = request.POST['pass']
        else:
            messages.error(request, 'error in password ')


        #check the values
        if  email and username and password:
            
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'the user name is taken')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'the email is taken')
                    else:
                        user = User.objects.create_user(
                            email=email, username=username, password=password)
                        user.save()
                        #add user profile
                        userprofile = UserProfile(
                            user=user)
                        userprofile.save()
                        # clear fields
                        email=''
                        username=''
                        password=''
                        #success 
                        messages.success(request, 'your account is create')
                        is_added = True

        else:
            messages.error(request, 'empty field')
        return render(request, 'accounts/signup.html', {
            'email': email,
            'user': username,
            'pass': password,
            'is_added': is_added
        })
    else:
        return render(request, 'accounts/signup.html')
