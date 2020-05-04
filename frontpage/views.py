from django.shortcuts import render


def exams_list(request):
    return render(request, 'frontpage/exams_list.html', {})
