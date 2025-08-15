from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from . models import CustomUser, UserProfile

class SystUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, max_length=254, help_text='Enter your email address.')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Your First Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Your Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Your Email address'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Choose a Username to Use'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Your Prefered Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Re-enter Your Password'
    }))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2  # SystUser
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'bio', 'profile_picture']

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        if commit:
            user.save()
            profile.save()
        return profile

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control text-center', 'placeholder': 'Enter Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control text-center', 'placeholder': 'Enter Your Password'}))