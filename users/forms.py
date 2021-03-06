from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()
  island_boi = forms.CharField(
        label="Do you know how to play chess?",
        max_length=90,
        widget=forms.TextInput(),
        required=True,
    )

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image']