from django.shortcuts import render
from .models import Exame
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExameForm


def post_list(request):
    return render(request, 'frontpage/post.html', {})


def formulario(request):
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            teste = form.save()
        return redirect('teste_cognitivo', pk=Exame.pk)
    else:
        form = ExameForm()
    return render(request, 'frontpage/formulario.html', {'form': form})


def teste_cognitivo(request, pk):
    pk = Exame.objects.get(pk=pk)
    if request.method == 'POST':
        test = ExameForm(request.POST)
        if test.is_valid():
            teste = test.save()
            return redirect('respostas/<int:pk>/', pk)
    else:
        test = ExameForm()
    return render(request, 'frontpage/teste_cognitivo.html', {'test': test})


def respostas(request, pk):
    results = Exame.objects.get(pk=pk)
    return render(request, 'frontpage/resultados.html', {'results': results})
