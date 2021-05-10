from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class SimpleUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = SimpleUser
        fields = ('email', 'username', 'first_name', 'last_name')

class SimpleUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password')

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'