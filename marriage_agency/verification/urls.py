# verification/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_verification, name='upload_verification'),
]
