from django import forms

class DocumentForm(forms.Form):
    attfile = forms.ImageField()
