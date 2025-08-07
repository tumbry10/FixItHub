from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SystUserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_syst_user(request):
    if request.method == 'POST':
        form = SystUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = SystUserRegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')