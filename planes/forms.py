from django import forms
from .models import PlanEntrenamiento

class PlanEntrenamientoBaseForm(forms.ModelForm):
    class Meta:
        model = PlanEntrenamiento
        fields = ['nombre', 'descripcion', 'duracion_semanas', 'precio', 'nivel', 'cupo_maximo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion_semanas': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'nivel': forms.Select(attrs={'class': 'form-select'}),
            'cupo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PlanEntrenamientoCrearForm(PlanEntrenamientoBaseForm):
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres.")
        if PlanEntrenamiento.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un plan con este nombre.")
        return nombre

class PlanEntrenamientoEditarForm(PlanEntrenamientoBaseForm):
    pass