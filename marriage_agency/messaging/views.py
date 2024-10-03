# messaging/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from .forms import MessageForm

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages': received_messages})

@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            messages.success(request, _('Your message has been sent!'))
            return redirect('chat', receiver_id=receiver.id)
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form, 'receiver': receiver})

@login_required
def chat(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    messages_qs = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=receiver)) |
        (models.Q(sender=receiver) & models.Q(receiver=request.user))
    ).order_by('timestamp')
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            messages.success(request, _('Your message has been sent!'))
            return redirect('chat', receiver_id=receiver.id)
    else:
        form = MessageForm()
    
    return render(request, 'messaging/chat.html', {'messages': messages_qs, 'form': form, 'receiver': receiver})
