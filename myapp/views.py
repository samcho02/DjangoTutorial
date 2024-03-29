from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # render(request, file_name, dictionary)
    features = Feature.objects.all()
    # render stuff in index.html
    return render(request, 'index.html', {'features' : features})

def register(request):
    # if clicked submit to post
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # filter through database to see if email exists
            if User.objects.filter(email=email).exists():
                # display message
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            # or same username
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used') 
                return redirect('register')
            # else create user
            else: 
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        
    else:
        return render(request, 'login.html')



def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

    