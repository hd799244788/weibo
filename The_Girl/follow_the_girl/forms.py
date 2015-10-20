from django import forms
from django.contrib.auth.models import User
from follow_the_girl.models import tb_counter, tb_follow_info

class UserForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email','password')
