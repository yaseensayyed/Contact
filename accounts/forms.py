from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 

class Registration(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20,required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name*'
        self.fields['first_name'].label = ''
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name*'
        self.fields['last_name'].label = ''
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email ID*'
        self.fields['email'].label = ''
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name*'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password*'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password*'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''
        
