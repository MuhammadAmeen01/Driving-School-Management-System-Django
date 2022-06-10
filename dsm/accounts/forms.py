from django import forms
from django.forms import TextInput
#from django.forms import Textarea
from .backend import AuthBackend
from .models import customer

# creating a form
'''class InputForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=13)
    password = forms.CharField(widget=forms.PasswordInput())'''


class MyForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ["name", "email", "phone", 'password_en']
        labels = {'name': "Name", "email": "Email", "phone": "Phone", "password_en": "Password"}

        widgets = {
            'email': TextInput(attrs={'class': 'container'}),
            'phone': TextInput(attrs={'class': 'container'})

        }

    '''def clean_name(self):

        product=AuthBackend.authenticate(self,username='name',password="123")
        print("hghg",product)
        if product is not None:

            raise forms.ValidationError("Username already exist")
        else:
            print("ok")'''

