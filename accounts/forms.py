from django import forms 
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

class SystUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2  # SystUser
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user