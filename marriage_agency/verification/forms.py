# verification/forms.py

from django import forms
from .models import ProfileVerification
from django.utils.translation import gettext_lazy as _

class VerificationForm(forms.ModelForm):
    class Meta:
        model = ProfileVerification
        fields = ['id_document']
        labels = {
            'id_document': _('Upload ID Document'),
        }
