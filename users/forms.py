# users forms 

from django import forms 

from users.models import Hotel, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError

# utilizacion de formularios 

class HotelForm(forms.ModelForm):
    
    class Meta:
        model = Hotel
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['picture', 'telefono', 'fecha_nacimiento', 'lugar_recidencia',]
        
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        
    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            
            raise ValidationError('This email address is already in use. Please supply a different email address.')
        return email

        
        
        
        