# verification/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ProfileVerification(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    id_document = models.FileField(_('ID Document'), upload_to='verification_docs/')
    verified = models.BooleanField(_('Verified'), default=False)
    verification_date = models.DateTimeField(_('Verification Date'), null=True, blank=True)

    def __str__(self):
        return f'{self.profile.username} - Verified: {self.verified}'
