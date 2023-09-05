from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


#custom imports
from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        

        if username:
            user = User.objects.filter(username = username)
            if user:
                context = {
                    'fullname' : full_name,
                    'username' : username,
                    'email' : email,
                    'error_username' : "Username taken",
                }
                return render(request, 'main/create_user.html', context)
        
        if email:
            user = User.objects.filter(email= email)
            if user:
                context = {
                    'fullname' : full_name,
                    'username' : username,
                    'email' : email,
                    'error_email' : "Email already in use",
                }
                return render(request, 'main/create_user.html', context)
    
        if password1 != password2:
            context = {
                    'fullname' : full_name,
                    'username' : username,
                    'email' : email,
                    'error_password' : "Password not matching",
            }
            return render(request, 'main/create_user.html', context)

        name_parts = full_name.split()
        if len(name_parts) >= 2:
            last_name = name_parts[-1]
            first_name = ' '.join(name_parts[:-1])
        else:
            first_name = ""
            last_name = full_name

        user = User(first_name=first_name,last_name=last_name,username=username,email=email)
        user.set_password(password1)
        user.save()
        messages.success(request, 'Registration Successful. Now login to your account')

        return redirect('user:login')

    elif request.method == "GET":
        return render(request, 'main/create_user.html')
    else:
        return HttpResponse("Request Method not allowed", status = 405)
    


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('apply:apply-institution')
        else:
            return redirect('user:login')

    elif request.method == "GET":
        return render(request, 'main/login.html')
    else:
        return HttpResponse("Request Method not allowed", status = 405)
    