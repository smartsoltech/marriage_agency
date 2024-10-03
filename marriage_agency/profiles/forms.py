# profiles/forms.py

from django import forms
from .models import Profile, GroomProfile, BrideProfile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)  # Добавляем поле

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password', 'date_of_birth']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user_type', 'first_name', 'last_name', 'date_of_birth', 'country', 'city', 'phone_number',
            'email', 'bio', 'photo', 'height', 'weight', 'religion', 'education',
            'occupation', 'hobbies', 'languages_spoken', 'looking_for', 'goals_in_relationship',
            'smoking', 'drinking', 'children', 'willingness_to_have_children', 'marital_status'
        ]
        labels = {
            'user_type': _('User Type'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'date_of_birth': _('Date of Birth'),
            'country': _('Country'),
            'city': _('City'),
            'phone_number': _('Phone Number'),
            'email': _('Email'),
            'bio': _('Bio'),
            'photo': _('Photo'),
            'height': _('Height'),
            'weight': _('Weight'),
            'religion': _('Religion'),
            'education': _('Education'),
            'occupation': _('Occupation'),
            'hobbies': _('Hobbies'),
            'languages_spoken': _('Languages Spoken'),
            'looking_for': _('Looking For'),
            'goals_in_relationship': _('Goals in Relationship'),
            'smoking': _('Smoking'),
            'drinking': _('Drinking'),
            'children': _('Children'),
            'willingness_to_have_children': _('Willingness to have Children'),
            'marital_status': _('Marital Status'),
        }
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('First Name')}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last Name')}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Country')}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('City')}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Phone Number')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Bio')}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Height')}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Weight')}),
            'religion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Religion')}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Education')}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Occupation')}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': _('Hobbies')}),
            'languages_spoken': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Languages Spoken')}),
            'looking_for': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': _('Looking For')}),
            'goals_in_relationship': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Goals in Relationship')}),
            'smoking': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'drinking': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'children': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'willingness_to_have_children': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
        }

class GroomProfileForm(forms.ModelForm):
    class Meta:
        model = GroomProfile
        fields = ['income_level', 'housing_status', 'car']
        labels = {
            'income_level': _('Income Level'),
            'housing_status': _('Housing Status'),
            'car': _('Car'),
        }

class BrideProfileForm(forms.ModelForm):
    class Meta:
        model = BrideProfile
        fields = ['has_children', 'education_level']
        labels = {
            'has_children': _('Has Children'),
            'education_level': _('Education Level'),
        }
