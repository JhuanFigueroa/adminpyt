from django import forms
from .models import Actividad


class ActividadForm(forms.ModelForm):
    """Form definition for Actividad."""

    class Meta:
        """Meta definition for Actividadform."""

        model = Actividad
        fields = ('nombre',
        'fecha',
        'participantes',
        'objetivo',
        'descripcion',
        'categoria',
        'imagen')

        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Nombre de la actividad',
                    'id':'nombre_actividad'
                }
            ),
            'fecha':forms.DateInput(
                attrs={
                    'type':'date'
                }
            ),
            'participantes':forms.NumberInput(
                attrs={
                    'placeholder':'N° participantes',
                    'id':'participantes_actividad'
                }
            ),
            'objetivo':forms.Textarea(
                attrs={
                    'placeholder':'Objetivo de la actividad',
                    'cols':'30',
                    'rows':'20',
                    'id':'objetivo_actividad'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'id':'categoria_actividad'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'placeholder':'Descripcion de la actividad',
                    'cols':'30',
                    'rows':'20',
                    'id':'descripcion_actividad'
                    
                }
            ),
            'imagen':forms.ClearableFileInput(
                
            ),
               
        }
