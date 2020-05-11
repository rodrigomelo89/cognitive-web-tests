from django.shortcuts import render
from .models import Exame
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExameForm, ResultsForm


def post_list(request):
    return render(request, 'frontpage/post.html', {})


def formulario(request):
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            formComp = form.save()
            return redirect('teste_cognitivo', pk=formComp.pk)
    else:
        form = ExameForm()
    return render(request, 'frontpage/formulario.html', {'form': form})


def teste_cognitivo(request, pk):
    result = get_object_or_404(Exame, pk=pk)
    if request.method == 'POST':
        teste = ResultsForm(request.POST, instance=result)
        if teste.is_valid():
            resultsComp = teste.save()
            return redirect('respostas', pk=resultsComp.pk)
    else:
        teste = ResultsForm(instance=result)
    return render(request, 'frontpage/teste_cognitivo.html', {'test': teste})


def respostas(request, pk):
    results = get_object_or_404(Exame, pk=pk)
    return render(request, 'frontpage/resultados.html', {'results': results})
