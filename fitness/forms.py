from django import forms
from django.forms import Form, ModelForm
from .models import Abonnement


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'label': ''
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nom'
        self.fields['password'].label = 'Mot de passe'
        self.fields['username'].widget.attrs['placeholder'] = "nom d'utilisateur"
        self.fields['password'].widget.attrs['placeholder'] = 'mot de passe'


class AbonnementForm(ModelForm):
    class Meta:
        model = Abonnement
        fields = ['client', 'offer']

    def __init__(self, *args, **kwargs):
        super(AbonnementForm, self).__init__(*args, **kwargs)
        self.fields['client'].label = "Le client:"
        self.fields['offer'].label = "L'offre:"
        self.fields['client'].widget.attrs['placeholder'] = "nom du client"
        self.fields['offer'].widget.attrs['placeholder'] = "l'offre"
