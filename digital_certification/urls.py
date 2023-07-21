from django.urls import path
from . import views

urlpatterns = [
    path('certificate/', views.certificate_list, name='certificate_list'),
    path('certificate/<int:certificate_id>/', views.certificate_detail, name='certificate_detail'),
]
