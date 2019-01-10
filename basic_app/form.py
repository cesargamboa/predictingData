from django import forms
from django.core import validators


class Decease(forms.Form):
    ED = forms.DecimalField()
    DEL = forms.DecimalField()
    NP = forms.DecimalField()
    PL = forms.DecimalField()
    CE = forms.DecimalField()
    CCS = forms.DecimalField()
    SCCS = forms.DecimalField()

