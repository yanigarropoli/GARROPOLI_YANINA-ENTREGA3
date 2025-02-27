from django import forms

from inicio.models import Vinos

class CargarVinos(forms.Form):
    variedad = forms.CharField(max_length=30)
    etiqueta = forms.CharField(max_length=30)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    imagen = forms.ImageField(required=False)
    



class FiltroVino(forms.Form):
    variedad = forms.CharField(max_length=100, required=False, label="Variedad")
    

class EditarVinoFormulario(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    imagen = forms.ImageField(required=False)
    
    class Meta:
        model = Vinos
        fields = '__all__'