from django import forms

class QRCodeForm(forms.Form):
    organisation_name = forms.CharField(
        max_length=50,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Enter URL Name'
        })
        )
    url = forms.URLField(
        max_length=200, 
        label='Enter URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Enter URL'
        })
        )