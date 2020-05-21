# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import sys
sys.path.insert(1,'C:\\Users\\digo_\\Documents\\Codes\\fluencia-NAO\\codes')  # pra poder fazer os imports de outro dir

import fluencia, recording_pc, ggl_code
from django.shortcuts import render
from .models import Exame
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExameForm


# trans = None  # variavel global pra salvar a transcrição
audio = None  # variavel global pra salvar o caminho do audio

def post_list(request):  # página inicial
    return render(request, 'frontpage/post.html', {})


def formulario(request):  # página de formulário
    if request.method == 'POST':  # pra requerer o formulário
        form = ExameForm(request.POST)  # abre o form
        if form.is_valid():  # verifica se os campos foram preenchidos
            formComp = form.save()  # salva o formulário
            # redireciona para a próxima página, o pk (primary key) do paciente vai tá vinculado ao form
            return redirect('teste_cognitivo', pk=formComp.pk)
    else:
        form = ExameForm()  # pra manter exibindo a página do form sem tá preenchido
    return render(request, 'frontpage/formulario.html', {'form': form})


def teste_cognitivo(request, pk):  # página onde será realizado o teste de fluencia verbal
    results = get_object_or_404(Exame, pk=pk)  # pega os dados do paciente q preencheu o formulário na pag anterior
    if request.method == 'POST':  # aguarda o botão ser clicado
        # TODO ajustar o tempo na chamada da função de gravação
        global audio  # acessa a variavel global
        audio = recording_pc.recording_mic(5, 'experiment', results.paciente)  # grava o áudio que será usado
        # redireciona pra página onde será exibido os resultados
        return redirect('respostas', pk=results.pk)
    # pra exibir a página do teste
    return render(request, 'frontpage/teste_cognitivo.html', {})


def respostas(request, pk):  # página onde será exibido os resultados
    result = Exame.objects.get(pk=pk)  # busca os dados do paciente correto
    global audio  # acessa a variavel global
    trans = ggl_code.transcribe_file(audio)  # reconhece o audio e salva o resultado na variavel global
    result.transcri = trans.results[0].alternatives[0].transcript  # salva a transcrição na ficha do paciente
    lista_palavras = fluencia.distinguish_words(result.transcri)  # separa as palavras identificadas numa lista
    result.nota, result.resultados = fluencia.fluencia(lista_palavras)  # calcula a pontuação do teste e salva os
                                                                      # animais reconhecidos
    result.save()
    # exibe a página de resultados
    return render(request, 'frontpage/resultados.html', {'results': result.resultados, 'palavras': result.transcri,
                                                         'nota': result.nota})
