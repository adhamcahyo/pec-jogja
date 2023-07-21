from django.shortcuts import render
from .models import StudentPerformance

def analytics_dashboard(request):
    student_performances = StudentPerformance.objects.all()
    return render(request, 'learning_analytics/templates/analytics_dashboard.html', {'student_performances': student_performances})