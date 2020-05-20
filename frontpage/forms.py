from django import forms
from .models import Exame


class ExameForm(forms.ModelForm):  # formulário

    class Meta:
        model = Exame  # busca o modelo
        fields = ('paciente', 'idade', 'tempo_estudo', 'genero',)  #dados a serem preenchidos




