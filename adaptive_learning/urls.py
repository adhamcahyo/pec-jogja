from django.urls import path
from . import views

urlpatterns = [
    path('adaptive_course/', views.adaptive_course_list, name='adaptive_course_list'),
    path('adaptive_course/<int:course_id>/', views.adaptive_course_detail, name='adaptive_course_detail'),
]