from django import forms
from django.forms import widgets
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = ['cliente', 'mesa']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'
        self.fields['data'].widget = widgets.DateInput({'type': 'date'})
        self.fields['hora'].widget = widgets.TimeInput({'type': 'time'})
        
        
