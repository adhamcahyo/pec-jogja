from django.shortcuts import render
from .models import MachineLearningAssessment

def assessment_list(request):
    assessments = MachineLearningAssessment.objects.all()
    return render(request, 'machine_learning_assessmenta/templates/ssessment_list.html', {'assessments': assessments})

def assessment_detail(request, assessment_id):
    assessment = MachineLearningAssessment.objects.get(pk=assessment_id)
    return render(request, 'machine_learning_assessment/templates/assessment_detail.html', {'assessment': assessment})