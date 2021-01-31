from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from business.models import (
    User,
    Profile, 
    BusinessComment,
    Businessuser
)
class BusinessSignUpForm(UserCreationForm):
    
    email= forms.EmailField()
    business_phone_number=forms.IntegerField()
    Accept_Terms_and_Conditions = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'email', 'business_phone_number' ,'password1', 'password2', 'Accept_Terms_and_Conditions']

    def save(self):
        user = super().save(commit=False)
        user.is_business = True
        user.save()
        return user

        
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    Accept_Terms_and_Conditions = forms.BooleanField()
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1', 'password2', 'Accept_Terms_and_Conditions']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_justuser = True
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'location', 'facebook', 'instagram', 'twitter']


class CreateBusinessComment(forms.ModelForm):
    class Meta:
        model = BusinessComment
        fields = ['message']

class CreateBusinessuser(forms.ModelForm):
    class Meta:
        model = Businessuser
        fields = ['product','service','food', 'about_business']


