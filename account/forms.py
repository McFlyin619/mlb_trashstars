from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = '@'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['team']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['team'].label = 'Pick a team'