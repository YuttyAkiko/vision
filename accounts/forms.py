from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email']