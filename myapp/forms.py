from .models import Booking 
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking       # Vincula el formulario al modelo Booking
        fields = "__all__"    # Incluye automáticamente todos los campos del modelo
    pass

