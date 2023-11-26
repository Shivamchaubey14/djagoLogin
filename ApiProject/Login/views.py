from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


def register(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        if password == confirm_password:

            user = User.objects.create_user(username=username, email=email, password=password, )
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('login')
        else:
            error_message = "Password didn't match"
    return render(request, 'register.html', {error_message: error_message})



def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password=password)
        if user is not None:
            return redirect('success')
        else:
            return redirect('invalid')
    return render(request, 'login.html')
        
def success(request):
    return render(request, 'success.html')

def invalid(request):
    return render(request, 'invalid.html')