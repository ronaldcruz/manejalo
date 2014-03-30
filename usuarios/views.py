# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from usuarios.forms import SignUpForm, LoginForm, RecoveryForm
from usuarios.models import Usuario

import uuid



def login(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user = Usuario.objects.get(email=form.cleaned_data['email'])
            if user.check_password(form.cleaned_data['password']):
                return redirect(reverse('home'))

        else:
            messages.error(request, 'El correo o la contraseña ingresados son inválidos.')
    else:

        initial_data = {
            'email': '',
            'password': ''
        }

        form = LoginForm(initial=initial_data) # An unbound form

    return render(request, 'login.html', {
        'form': form,
    })

    

def signup(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = SignUpForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return redirect(reverse('home')) # Redirect after POST

        else:
            messages.error(request, 'Algunos de los campos esta incorrecto o hace falta información.')
            
    else:

        initial_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': str(uuid.uuid1())
        }

        form = SignUpForm(initial=initial_data) # An unbound form

    return render(request, 'signup.html', {
        'form': form,
    })
    

def recovery(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = RecoveryForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            messages.success(request, 'Se ha enviado un mensaje a su correo electrónico.')
            return redirect(reverse('home')) # Redirect after POST

    else:

        initial_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': str(uuid.uuid1())
        }

        form = SignUpForm(initial=initial_data) # An unbound form

    return render(request, 'recovery.html', {
        'form': form,
    })


