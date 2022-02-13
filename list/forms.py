import imp
from django import forms
from .models import Home
from captcha.fields import ReCaptchaField
class HomeForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = ['tittle', 'description']

    captcha = ReCaptchaField()
    