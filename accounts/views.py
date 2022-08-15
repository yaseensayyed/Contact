from django.shortcuts import render, redirect
from .forms import Registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'base.html')

def SignUp(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"Registration successful")
            return redirect('login')
        else:
            messages.error(request,"Unsuccessful registration!! Invalid information")
    else:
        form = Registration()
        messages.info(request,"Fill this form to become a User!!")
    return render(request=request, template_name='signup.html', context={"signup":form})

def dash(request):
    return render(request, 'dashboard.html')

def LogIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('dashboard')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
        messages.info(request,"Kindly enter your credentials!!")
    return render(request=request, template_name="login.html", context={'login':form})

def LogOut(request):
    logout(request)
    messages.error(request,"Successfully Logged out!!")
    return redirect('home')
    
    