from django.shortcuts import render
from .models import Exams


def exams_list(request):
    exames = Exams.objects.order_by('idade')
    return render(request, 'frontpage/exams_list.html', {'exames': exames})
