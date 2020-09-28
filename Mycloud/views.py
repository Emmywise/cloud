from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Mycloud.form import SignUpForm, UserLoginForm, DocumentForm, ImageForm
from Mycloud.models import Document, ImageUpload #to import the fileupload model
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth import logout
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request,'Mycloud/index.html')

@login_required
def home(request):
    documents = Document.objects.filter(user=request.user)
    images = ImageUpload.objects.all()
    return render(request, 'Mycloud/home.html', {
        "documents": documents, "images": images
    })

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
        user = authenticate(username=username, password=password) #authenticate confirm if username and password correspond
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Mycloud:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Mycloud/login.html', {'form': form})

    @login_required #trying to use decorator, though the login code didnt get here
    def special(request):
        return HttpResponse("You are logged in !")

def user_logout(request):# users logout function
    logout(request)
    #return HttpResponse("You are logged out !")# logout function end here
    return redirect('Mycloud:index') # just a line i choose to add in case i decide to redirect to index page

@login_required
def upload(request): #function for users to upload files
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES) #expect  a doc
        if form.is_valid():
            #form.save()
            newdoc = Document(document = request.FILES['document'])
            newdoc.user = request.user
            
            form=newdoc.save()
            #documents = form.instance
            #return render(request, Mycloud/home.html, {'form':form, 'documents':documents})
            return redirect('Mycloud:home')
    else:
        form = DocumentForm()
    return render(request, 'Mycloud/upload.html', {  'form': form }) 

@login_required
def imageupload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('Mycloud:home')
    else:
        form = ImageForm
    return render(request, 'Mycloud/imageupload.html', {  'form': form } )

def delete_file(request, pk):
    if request.method == "POST":
        documents = Document.objects.get(pk=pk)
        documents.delete()
    return redirect('Mycloud:home')


def delete_image(request, pk):
    if request.method == "POST":
        images = ImageUpload.objects.get(pk=pk)
        images.delete()
    return redirect('Mycloud:home')

