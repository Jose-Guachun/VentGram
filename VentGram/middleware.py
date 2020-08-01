#Ventgram middleware

from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
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
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')

        response = self.get_response(request)
        return response