from django.shortcuts import render
from .models import CourseSentiment

def course_sentiment_detail(request, course_id):
    course_sentiment = CourseSentiment.objects.get(course_id=course_id)
    return render(request, 'sentiment_analysis/templates/sentiment_analysis_course_detail.html', {'course_sentiment': course_sentiment})