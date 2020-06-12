# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import pyaudio
import wave
import os


def printou(name):
    print("funcionou", name)


def recording_mic(s, experiment, namefile):
    # função para gravar o audio
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1  # número de canais usados
    fs = 16000  # Record at 44100 samples per second
    chunk = 1024  # int(fs / 10)  # Record in chunks of 1024 samples
    seconds = s
    filename = namefile + ".wav"  # salvar como .WAV
    # os.path.join(r'C:\Users\Rodrigo Melo\Documents\fluencia-NAO\audios', filename)

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')
    # grava com essa configuração abaixo
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    file_path = "C:\\Users\\digo_\\Documents\\Codes\\fluencia-NAO\\audios\\" + experiment + "\\" + filename
    wf = wave.open(file_path, 'wb')
    # (os.path.join(r'C:\Users\Rodrigo Melo\Documents\fluencia-NAO\audios', experiment + filename), 'wb')
    wf.setnchannels(channels)
    print(p.get_sample_size(sample_format))
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    return file_path
