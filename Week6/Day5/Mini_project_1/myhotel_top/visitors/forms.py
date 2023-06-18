from django import forms
from .models import Booking, Message


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        exclude = ('room',)

        widgets = {
            'check_in': DateInput(attrs={'class': 'form-control'}),
            'check_out': DateInput(attrs={'class': 'form-control'}),
        }


class FilterForm(forms.ModelForm):

    class Meta:
        model = Booking
        exclude = ('room', 'guest')

        widgets = {
            'check_in': DateInput(attrs={'class': 'form-control'}),
            'check_out': DateInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'