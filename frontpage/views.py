# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import sys
sys.path.insert(1,'C:\\Users\\digo_\\Documents\\Codes\\fluencia-NAO\\codes')  # pra poder fazer os imports de outro dir

import fluencia, recording_pc, ggl_code
from django.shortcuts import render
from .models import Exame
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExameForm, TestForm
from django.http import HttpResponse


# trans = None  # variavel global pra salvar a transcrição
file_path = 'C:\\Users\\digo_\\Documents\\Codes\\fluencia-NAO\\codes\\media\\'  # variavel global pra salvar o caminho do audio


def post_list(request):  # página inicial
    return render(request, 'frontpage/post.html', {})


def formulario(request):  # página de formulário
    if request.method == 'POST':  # pra requerer o formulário
        form = ExameForm(request.POST)  # abre o form
        if form.is_valid():  # verifica se os campos foram preenchidos
            formComp = form.save()  # salva o formulário
            # redireciona para a próxima página, o pk (primary key) do paciente vai tá vinculado ao form
            return redirect('cognitive_webapp:teste', pk=formComp.pk)
    else:
        form = ExameForm()  # pra manter exibindo a página do form sem tá preenchido
    return render(request, 'frontpage/formulario.html', {'form': form})


def teste_cognitivo(request, pk):  # página onde será realizado o teste de fluencia verbal
    results = get_object_or_404(Exame, pk=pk)  # pega os dados do paciente q preencheu o formulário na pag anterior
    # print('to aqui', results.paciente, type(request.FILES.get(results.paciente)))
    if request.method == 'POST':  # aguarda o botão ser clicado
        # print("### chegou aqui ###")
        # print(request.FILES['banda'])
        global file_path
        file_path += results.paciente+'.wav'
        with open(file_path, 'wb+') as destination:
            for chunk in request.FILES['banda'].chunks():
                destination.write(chunk)
        # redireciona pra página onde será exibido os resultados
        return redirect('cognitive_webapp:respostas', pk=results.pk)
    # pra exibir a página do teste
    return render(request, 'frontpage/teste_cognitivo.html', {'paciente': results.paciente, 'key': pk})


def respostas(request, pk):  # página onde será exibido os resultados
    result = Exame.objects.get(pk=pk)  # busca os dados do paciente correto
    global file_path
    trans = ggl_code.transcribe_file(file_path)  # reconhece o audio
    # global file_path
    file_path = "C:\\Users\\digo_\\Documents\\Codes\\fluencia-NAO\\codes\\media\\"
    print(trans.results, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # result.transcri = trans.results[0].alternatives[0].transcript  # salva a transcrição na ficha do paciente
    # lista_palavras = fluencia.distinguish_words(result.transcri)  # separa as palavras identificadas numa lista
    # result.nota, result.resultados = fluencia.fluencia(lista_palavras)  # calcula a pontuação do teste e salva os
    #                                                                   # animais reconhecidos
    # result.save()
    # exibe a página de resultados
    return render(request, 'frontpage/resultados.html', {'results': result.resultados, 'palavras': result.transcri,
                                                         'nota': result.nota})
