from django import forms
from .models import Customer, Vehicle, Rental

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ('date_created',)
        
class RentalForm(forms.ModelForm):
    # add rental
    class Meta:
        model = Rental
        fields = '__all__'
        exclude = ('date_created','return_date')
        

class ReturnForm(forms.Form):
    isreturn = forms.ModelMultipleChoiceField(queryset=Rental.objects.all(),
                                                widget = forms.HiddenInput())
    
    # class Meta:
    #     model = Rental
    #     fields = ('return_date',)
    # widget = {'return_date': forms.HiddenInput()}
             