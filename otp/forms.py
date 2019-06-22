from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=200, help_text='Required', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'co'}))
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={'placeholder': 'E-Mail', 'class': 'co'}))
    password1 = forms.CharField(max_length=200, help_text='Required', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'co'}))
    password2 = forms.CharField(max_length=200, help_text='Required', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm_Password', 'class': 'co'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2')
