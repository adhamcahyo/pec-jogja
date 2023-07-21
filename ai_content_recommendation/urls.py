from django.urls import path
from . import views

urlpatterns = [
    path('recommended_courses/', views.recommended_courses, name='recommended_courses'),
]