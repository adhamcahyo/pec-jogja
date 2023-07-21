from django.shortcuts import render
from .models import VirtualClassroom

def virtual_classroom_list(request):
    virtual_classrooms = VirtualClassroom.objects.all()
    return render(request, 'virtual_classroom/virtual_classroom_list.html', {'virtual_classrooms': virtual_classrooms})

def virtual_classroom_detail(request, virtual_classroom_id):
    virtual_classroom = VirtualClassroom.objects.get(pk=virtual_classroom_id)
    return render(request, 'virtual_classroom/templates/virtual_classroom_detail.html', {'virtual_classroom': virtual_classroom})