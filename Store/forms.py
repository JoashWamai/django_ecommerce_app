from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, ShippingDetails


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': "UserName",
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': "Email",
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': "Password",
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': "ConfirmPassword",
            }),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['reviewText']
        widgets = {
            'reviewText': Textarea(attrs={'rows': 5})
        }


class ShippingDetailsForm(ModelForm):
    class Meta:
        model = ShippingDetails
        exclude = ["customer", "order"]
