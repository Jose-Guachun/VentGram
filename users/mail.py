from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.shortcuts import render

def send_email(mail, token):
    context={'mail': mail, 'token': token}

    template=get_template('users/correo.html')
    content=template.render(context)

    email=EmailMultiAlternatives(
        'VentGram, Activacion de Cuenta',
        'hola ue hace',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()