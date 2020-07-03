from pydub import AudioSegment
import pathlib


def convert2wav(file_in, file_out):  # entra path pro arquivo do site, sai path do arquivo salvo
    sound = AudioSegment.from_file(file_in)  # abre o arquivo de audio
    file_in = sound.set_sample_width(2)  # muda o numeros de bits por sample (1 = 8 bits, 2 = 16 bits, 4 = 32 bits)
    n = len(file_in)  # ver o tamanho do arquivo em milisegundos
    file_in.export(file_out, format='wav')  # salva o arquivo no formato wav
    return n

def split_audio(file_in):
    file_out = file_in.parent
    # print(file_out, file_in)
    myaudio = AudioSegment.from_wav(file_in)  # ler o arquivo de .wav
    n = len(myaudio)  # tamanho do audio em ms
    # print("n = ", n)
    interval = 30000  # 30 segundos de audio (padrão ms)
    overlap = 2000  # 2 segundos de overlap

    chunk1 = myaudio[0:interval]  # cria um audio com os primeiros 30 segundos
    file_1 = file_out/'chunk_1.wav'  # o endereço onde vai salvo o audio
    chunk1.export(file_1, format='wav')  # salva o audio
    chunk2 = myaudio[interval-overlap:n]  # cria um audio começando dos 28 até o final do audio original
    file_2 = file_out/'chunk_2.wav'
    chunk2.export(file_2, format='wav')

