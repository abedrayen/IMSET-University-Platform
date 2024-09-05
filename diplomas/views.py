from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Diploma

def generate_diploma(request, diploma_id):
    diploma = Diploma.objects.get(pk=diploma_id)
    if diploma.diploma_type == 'BTP':
        template_name = 'diplomas/btp_diploma.html'
    else:
        template_name = 'diplomas/bts_diploma.html'
    
    return render(request, template_name, {'student': diploma.student, 'diploma': diploma})

from django.shortcuts import render
from django.http import JsonResponse
from .models import Diploma


def preview_diploma(request, diploma_id):
    diploma = get_object_or_404(Diploma, id=diploma_id)
    if diploma.diploma_type == 'BTP':
        template_name = 'diplomas/btp_diploma.html'
    else:
        template_name = 'diplomas/bts_diploma.html'
    
    return render(request, template_name, {'student': diploma.student, 'diploma': diploma})


