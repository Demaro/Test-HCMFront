from django import forms
from django.forms import ModelForm
from .models import Reservacion


class ReservaForm(forms.ModelForm):
         
    class Meta:
        model = Reservacion

        fields = [
            'fecha',
            'hora_inicio',   
            'hora_termino',
            'capacidad',
            'insumos',

        ]
        labels = {  
            'fecha' : 'Fecha',
            'hora_inicio' : 'Inicio',
            'hora_termino': 'Termino',
            'capacidad'        : 'Cantidad Personas',
            'insumos'      : 'Cantidad Insumos',
        }
        widgets = {
            'fecha'      :       forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'hora_inicio':       forms.TextInput(attrs={'class': 'form-control'}),
            'hora_termino':      forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad':         forms.Select(attrs={'class': 'form-control'}),
            'insumos':       forms.Select(attrs={'class': 'form-control'})
        }
    