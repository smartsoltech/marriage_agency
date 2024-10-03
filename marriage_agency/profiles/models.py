# profiles/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('groom', _('Groom')),
        ('bride', _('Bride')),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(_('User Type'), max_length=10, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(_('Country'), max_length=100)
    city = models.CharField(_('City'), max_length=100)
    phone_number = models.CharField(_('Phone Number'), max_length=20, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    ])
    email = models.EmailField(_('Email'))
    bio = models.TextField(_('Bio'))
    photo = models.ImageField(_('Photo'), upload_to='profile_photos/', null=True, blank=True)

    height = models.DecimalField(_('Height'), max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(_('Weight'), max_digits=5, decimal_places=2, null=True, blank=True)
    religion = models.CharField(_('Religion'), max_length=50, null=True, blank=True)
    education = models.CharField(_('Education'), max_length=255, null=True, blank=True)
    occupation = models.CharField(_('Occupation'), max_length=255, null=True, blank=True)
    hobbies = models.TextField(_('Hobbies'), null=True, blank=True)
    languages_spoken = models.CharField(_('Languages Spoken'), max_length=255, null=True, blank=True)

    looking_for = models.TextField(_('Looking For'), null=True, blank=True)
    goals_in_relationship = models.CharField(_('Goals in Relationship'), max_length=255, null=True, blank=True)
    
    smoking = models.BooleanField(_('Smoking'), default=False)
    drinking = models.BooleanField(_('Drinking'), default=False)
    children = models.BooleanField(_('Children'), default=False)
    willingness_to_have_children = models.BooleanField(_('Willingness to have Children'), default=False)
    marital_status = models.CharField(_('Marital Status'), max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class GroomProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    income_level = models.DecimalField(_('Income Level'), max_digits=10, decimal_places=2)
    housing_status = models.CharField(_('Housing Status'), max_length=255, null=True, blank=True)
    car = models.BooleanField(_('Car'), default=False)

    def __str__(self):
        return f'Groom: {self.profile.first_name} {self.profile.last_name}'

class BrideProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    has_children = models.BooleanField(_('Has Children'), default=False)
    education_level = models.CharField(_('Education Level'), max_length=255)

    def __str__(self):
        return f'Bride: {self.profile.first_name} {self.profile.last_name}'
