from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .models import UserLoginLogout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import timedelta

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        login(request, user)
        UserLoginLogout.objects.create(user=user, login_time=timezone.now())
        return redirect('dashboard')
       
   
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    UserLoginLogout.objects.filter(user=request.user, logout_time=None).update(logout_time=timezone.now())
    logout(request)
    #return redirect('login')
    return render(request,'logout.html')
def index(request):
    usage = UserLoginLogout.objects.all()
    return render(request, 'index.html', {'usage': usage})
   # return render(request,"index.html",context)
   
def billing(request):
    return render(request,'billing.html')