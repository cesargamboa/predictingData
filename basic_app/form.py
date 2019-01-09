from django import forms
from django.core import validators


class Decease(forms.Form):
    num1 = forms.DecimalField()
    num2 = forms.DecimalField()
    num3 = forms.DecimalField()
    num4 = forms.DecimalField()
    num5 = forms.DecimalField()
    num6 = forms.DecimalField()

