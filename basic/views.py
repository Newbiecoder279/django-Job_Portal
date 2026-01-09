from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from jobs.models import PostJob
from . models import Profile
from django.db.models import Q


# Create your views here.
def home(request):
    jobs = PostJob.objects.all().order_by("created_at")
    context = {
        'jobs':jobs
    }
    return render(request,'home.html',context)


def registration(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                role = form.cleaned_data['role']
            )
            return redirect ('login')
    else:
        
        form = RegistrationForm()

    context = {
        'form':form
    }

    return render(request, 'registration.html', context)


def login(request):
   if request.method == 'POST':
      form = AuthenticationForm(request,request.POST)
      if form.is_valid():
       username = form.cleaned_data['username']
       password = form.cleaned_data['password']
       user = authenticate(request, username=username, password=password)

       if user is not None:
           auth_login(request, user)
           return redirect('dashboard')
   else:
       form = AuthenticationForm()
       
   context = {
    'form':form
    }
        
   return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')

def dashboard(request):
    return render(request,'dashboard.html')

def search(request):
    keyword = request.GET.get('keyword')
    jobs = PostJob.objects.filter(Q(title__icontains = keyword)|Q(job_type__icontains = keyword))

    context = {
        'keyword':keyword,
        'jobs':jobs
    }

    return render(request, 'search.html', context)       

       
       
           