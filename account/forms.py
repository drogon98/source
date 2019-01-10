from django import forms
from django.contrib.auth.models import User

class ChangeProfileForm(forms.ModelForm):
    username=forms.CharField(required=False)
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
