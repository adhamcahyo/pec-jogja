from django.urls import path
from . import views

urlpatterns = [
    path('sentiment_analysis/<int:course_id>/', views.course_sentiment_detail, name='course_sentiment_detail'),
]