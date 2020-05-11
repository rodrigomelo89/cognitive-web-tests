from django import forms
from .models import Exame


class ExameForm(forms.ModelForm):

    class Meta:
        model = Exame
        fields = ('paciente', 'idade', 'tempo_estudo', 'genero',)

    class Beta:
        model = Exame
        fields = ('resultados',)