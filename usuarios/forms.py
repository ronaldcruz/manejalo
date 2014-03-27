# -*- coding: utf-8 -*-
from django import forms
from usuarios.models import Usuario

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label=u"Nombre")
    last_name = forms.CharField(max_length=100, label=u"Apellido")
    username = forms.CharField(max_length=100, label=u"Usuario", required=False)
    email = forms.EmailField(label=u"Correo Electrónico")
    password = forms.CharField(max_length=100, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password']
    

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            user = Usuario.objects.get(email=email)
            if user:
                raise forms.ValidationError("El correo ingresado ya existe")
        except Usuario.DoesNotExist:
            pass

        return email


class LoginForm(forms.Form):
    email = forms.EmailField(label=u"Correo Electrónico")
    password = forms.CharField(max_length=100, label="Contraseña")


    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("El correo ingresado no existe")

        return email


class RecoveryForm(forms.Form):
    email = forms.EmailField(label=u"Correo Electrónico")
    

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("El correo ingresado no existe")

        return email
