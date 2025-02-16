from django import forms

class CargarVinos(forms.Form):
    variedad = forms.CharField(max_length=30)
    etiqueta = forms.CharField(max_length=30)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    


class FiltroVino(forms.Form):
    variedad = forms.CharField(max_length=100, required=False, label="Variedad")