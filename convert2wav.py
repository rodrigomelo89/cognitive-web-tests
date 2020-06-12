from pydub import AudioSegment


def convert2wav(file_in, file_out):  # entra path pro arquivo do site, sai path do arquivo salvo
    sound = AudioSegment.from_file(file_in)  # abre o arquivo de audio
    file_in = sound.set_sample_width(2)  # muda o numeros de bits por sample (1 = 8 bits, 2 = 16 bits, 4 = 32 bits)
    file_in.export(file_out, format='wav')  # salva o arquivo no formato wav

