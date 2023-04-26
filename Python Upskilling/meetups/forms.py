# region using ModelForm
# from django import forms 
# from .models import Participant 
 
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['email']
# endregion 

# region using Form

from django import forms
class RegistrationForm(forms.Form):
    email = forms.EmailField(label='User Email')
        
# endregion