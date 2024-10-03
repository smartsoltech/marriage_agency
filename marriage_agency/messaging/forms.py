# messaging/forms.py

from django import forms
from .models import Message
from django.utils.translation import gettext_lazy as _

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        labels = {
            'text': _('Message'),
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': _('Enter your message')}),
        }
