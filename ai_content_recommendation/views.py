 
from django.shortcuts import render
from .models import RecommendedCourse

def recommended_courses(request):
    recommended_courses = RecommendedCourse.objects.all()
    return render(request, 'ai_content_recommendation/templates/recommended_courses.html', {'recommended_courses': recommended_courses})