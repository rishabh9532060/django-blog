from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.user.is_authenticated :
        return redirect('dashboard')

    if request.method=="POST":
        username=request.POST.get('username','').strip()
        email=request.POST.get('email','').strip()
        password=request.POST.get('password','')
        confirm_password=request.POST.get('confirm_password','')

        if not username or not email or not password or not confirm_password:
            messages.error(request,'All fields are required')
            return render(request,'register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username Already exist')
            return render(request,'register.html')

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request,'User Created Success!!')
        return redirect('login')
    else:
        return render(request,'register.html')


def login_view(request):
    if request.user.is_authenticated :
            return redirect('dashboard')

    if request.method=="POST":
        username=request.POST.get('username','').strip()
        password=request.POST.get('password','')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"login success")
            return redirect('dashboard')

        else:
            messages.error(request,'wrong emailor password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
  
    logout(request)
    messages.success(request, "Successfully logout ho gaye!")
    return redirect('login')
    



@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')



