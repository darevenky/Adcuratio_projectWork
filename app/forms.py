from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        widgets={'password':forms.PasswordInput}
        help_text={'username':''}

class BirdsForm(forms.ModelForm):
    class Meta:
        model=Birds
        fields='__all__'
        #widgets={'about':forms.TextInput(attrs={'cols':50, 'rows':5})}