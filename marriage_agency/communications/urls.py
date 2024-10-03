# communications/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('video_call/<int:receiver_id>/', views.initiate_video_call, name='initiate_video_call'),
    path('video_call/<str:call_id>/', views.video_call_room, name='video_call_room'),
]
