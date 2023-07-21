from django.urls import path
from . import views

urlpatterns = [
    path('virtual_classroom/', views.virtual_classroom_list, name='virtual_classroom_list'),
    path('virtual_classroom/<int:virtual_classroom_id>/', views.virtual_classroom_detail, name='virtual_classroom_detail'),
]