# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import io
import utils
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from google.cloud.speech_v1 import types


def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    client = speech_v1.SpeechClient()  # cria o cliente da API do google

    with io.open(speech_file, 'rb') as audio_file:  # abre o arquivo de audio
        content = audio_file.read()  # ler o conteudo
        audio = types.RecognitionAudio(content=content)  # define o tipo

    config = types.RecognitionConfig(  # configuração a ser usada no reconhecimento
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='pt-BR',
        speech_contexts=[{"phrases": utils.list_animals}]  # dica para reconhecimento
    )

    response = client.recognize(config, audio)  # reconhecimento do audio

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    # for result in response.results:
    #     # The first alternative is the most likely one for this portion.
    #     print(u'Transcript: {}'.format(result.alternatives[0].transcript))

    return response




