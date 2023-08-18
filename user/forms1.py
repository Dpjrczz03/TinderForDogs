from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=("Pet's name"))
    email = forms.EmailField(max_length=50,label=("Owner's Email"),
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter Owner's Email ID"})))
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label=("Pet's name"))
    email=forms.EmailField(max_length=50,label=("Owner's Email"),
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter Owner's Email ID"})))
    class Meta:
        model=User
        fields=['username','first_name','email']
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['bio', 'image']

class GenderForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender']