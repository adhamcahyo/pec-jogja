from django.shortcuts import render
from .models import Certificate

def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'digital_certification/certificate_list.html', {'certificates': certificates})

def certificate_detail(request, certificate_id):
    certificate = Certificate.objects.get(pk=certificate_id)
    return render(request, 'digital_certification/templates/certificate_detail.html', {'certificate': certificate})