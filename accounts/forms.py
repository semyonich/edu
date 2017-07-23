from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=5, max_length=255, widget=forms.TextInput(attrs={'type': 'password'}))