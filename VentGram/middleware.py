1#platzigram middleware

from django.shortcuts import redirect
from django.urls import reverse

class SignUpBlockMiddleware:
    #Middleware de finalización de perfil.
    # Asegúrese de que cada usuario que interactúa con la plataformatienen su foto de perfil y biografía.
    def __init__(self, get_response):
        """inicializacion del middleware"""
        self.get_response =get_response
    

    def __call__(self, request):
        """Código a ejecutar para cada solicitud antes de que se llame a 
            la vista."""
        if not request.user.is_anonymous:
            if  not request.user.is_staff:
                    if request.path in [reverse('users:signup'), reverse('posts:home')]:
                        return redirect('posts:feed')
        response = self.get_response(request)
        return response


