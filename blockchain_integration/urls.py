from django.urls import path
from . import views

urlpatterns = [
    path('transcript_verification/<int:transcript_id>/', views.transcript_verification, name='transcript_verification'),
]