from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lms_app.urls')),
    path('authentication/', include('authentication.urls')),
    path('adaptive_learning/', include('adaptive_learning.urls')),
    path('sentiment_analysis/', include('sentiment_analysis.urls')),
    path('virtual_classroom/', include('virtual_classroom.urls')),
    path('machine_learning_assessment/', include('machine_learning_assessment.urls')),
    path('project_based_learning/', include('project_based_learning.urls')),
    path('digital_certification/', include('digital_certification.urls')),
    path('ai_content_recommendation/', include('ai_content_recommendation.urls')),
    path('learning_analytics/', include('learning_analytics.urls')),
    path('blockchain_integration/', include('blockchain_integration.urls')),
]