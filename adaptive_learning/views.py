from django.shortcuts import render
from .models import AdaptiveCourse, AdaptiveLesson

def adaptive_course_list(request):
    courses = AdaptiveCourse.objects.all()
    return render(request, 'adaptive_learning/adaptive_course_list.html', {'courses': courses})

def adaptive_course_detail(request, course_id):
    course = AdaptiveCourse.objects.get(pk=course_id)
    lessons = AdaptiveLesson.objects.filter(course=course)
    return render(request, 'adaptive_learning/templates/adaptive_course_detail.html', {'course': course, 'lessons': lessons})