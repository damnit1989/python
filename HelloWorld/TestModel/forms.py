# -*- coding: utf-8 -*-
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_pswd = forms.CharField(label='Your pswd', max_length=100)

