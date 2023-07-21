from django.urls import path
from . import views

urlpatterns = [
    path('assessment/', views.assessment_list, name='assessment_list'),
    path('assessment/<int:assessment_id>/', views.assessment_detail, name='assessment_detail'),
]