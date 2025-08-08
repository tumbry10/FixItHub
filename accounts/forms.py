from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from . models import CustomUser, UserProfile

class SystUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, max_length=254, help_text='Enter your email address.')

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