from django import forms


class CursoFormulario(forms.Form):

    cursos = forms.CharField()
    camada = forms.IntegerField()