# messaging/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('send/<int:receiver_id>/', views.send_message, name='send_message'),
    path('chat/<int:receiver_id>/', views.chat, name='chat'),
]
