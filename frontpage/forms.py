from django import forms
from .models import Exame


class ExameForm(forms.ModelForm):  # formulário

    class Meta:
        model = Exame  # busca o modelo
        fields = ('nome_completo', 'idade', 'tempo_de_estudo', 'genero',)  #dados a serem preenchidos


class TestForm(forms.ModelForm):

    class Meta:
        model = Exame
        fields = ('audioRecorded',)