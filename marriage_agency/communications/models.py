# communications/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class VideoCall(models.Model):
    caller = models.ForeignKey(User, related_name='video_calls_made', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='video_calls_received', on_delete=models.CASCADE)
    call_id = models.CharField(_('Call ID'), max_length=100, unique=True)
    start_time = models.DateTimeField(_('Start Time'), auto_now_add=True)
    end_time = models.DateTimeField(_('End Time'), null=True, blank=True)
    status = models.CharField(_('Status'), max_length=20, choices=[
        ('initiated', _('Initiated')),
        ('ongoing', _('Ongoing')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    ], default='initiated')

    def __str__(self):
        return f'VideoCall {self.call_id} between {self.caller.username} and {self.receiver.username}'
