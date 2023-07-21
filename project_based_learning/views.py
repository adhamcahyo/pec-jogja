from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_based_learning/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'project_based_learning/templates/project_detail.html', {'project': project})