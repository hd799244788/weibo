from django import forms
from django.contrib.auth.models import User
from follow_the_girl.models import tb_counter, tb_follow_info

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    #email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'password')
