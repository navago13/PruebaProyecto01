from django import forms

class FormulariodeContacto(forms.Form):

    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()