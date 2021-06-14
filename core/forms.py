from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'
