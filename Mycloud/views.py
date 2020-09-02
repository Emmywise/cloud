from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Mycloud.form import SignUpForm, UserLoginForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'Mycloud/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            messages.success(request, 'Account created successfully')
            username = form.cleaned_data.get('username') 
            raw_password = form.cleaned_data.get('password1')
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect( 'Mycloud:login' )
        else:
            return render(request, 'Mycloud/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'Mycloud/signup.html', {'form': form})

def user_login(request):
    form = UserLoginForm(request.POST)
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Mycloud:home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Mycloud/login.html', {'form': form})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

def home(request):
    return render(request, 'Mycloud/home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    