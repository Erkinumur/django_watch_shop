from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from catalog.models import Review


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']