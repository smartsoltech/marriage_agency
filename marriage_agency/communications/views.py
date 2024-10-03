# communications/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VideoCall
from django.contrib import messages
import uuid
from django.conf import settings

@login_required
def initiate_video_call(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    
    # Проверка на тарифный план и доступность услуги
    # Здесь можно добавить логику проверки, доступна ли функция видеозвонков пользователю

    call_id = str(uuid.uuid4())
    video_call = VideoCall.objects.create(
        caller=request.user,
        receiver=receiver,
        call_id=call_id,
        status='initiated'
    )
    # Здесь можно интегрировать API видеозвонков, например, Twilio или Jitsi
    # Для простоты будем использовать простую ссылку на комнату
    return redirect('video_call_room', call_id=call_id)

@login_required
def video_call_room(request, call_id):
    video_call = get_object_or_404(VideoCall, call_id=call_id)
    if request.user not in [video_call.caller, video_call.receiver]:
        messages.error(request, _('You are not authorized to join this video call.'))
        return redirect('home')
    
    # Здесь можно интегрировать реальные видеозвонки через сторонние сервисы
    # Например, предоставив ссылку на комнату Jitsi Meet с идентификатором call_id
    jitsi_url = f'https://meet.jit.si/{call_id}'
    return render(request, 'communications/video_call_room.html', {'jitsi_url': jitsi_url, 'video_call': video_call})
