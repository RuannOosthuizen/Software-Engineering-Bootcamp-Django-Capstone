from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('homepage') # replace with the URL name of your home page
    else:
        login(request, user)
        error_message = "Invalid login credentials. Please try again."
        return render(request, 'login.html', {'error_message': error_message})