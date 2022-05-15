# users forms 

from django import forms 

from users.models import Hotel, Profile

# utilizacion de formularios 

class HotelForm(forms.ModelForm):
    
    class Meta:
        model = Hotel
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('picture',)