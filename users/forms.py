# users forms 

from django import forms 

from users.models import Hotel

# utilizacion de formularios 

class HotelForm(forms.ModelForm):
    
    class Meta:
        model = Hotel
        fields = '__all__'