from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'email']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']

""" from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email'] """