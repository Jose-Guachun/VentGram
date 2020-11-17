1#platzigram middleware

from django.shortcuts import redirect
from django.urls import reverse

from users.models import User
from posts.models import Project
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
                    if request.user.is_verified:
                        if request.path in [reverse('users:signup'), reverse('posts:home'), reverse('users:validate_token')]:
                            return redirect('posts:feed')
                    else:
                        
                        users=User.objects.all()
                        for user in users:
                            if request.path in[
                                reverse('users:detail', args=[user.username] ),
                                reverse('iteractions:messages', args=[user.username] ),
                                reverse('iteractions:directs', args=[user.username] ),
                                reverse('iteractions:newconversation', args=[user.username] ),
                                ]:
                                return redirect('users:validate_token')

                        projects=Project.objects.all()
                        for project in projects:
                            if request.path in[
                                reverse('posts:detail_project', args=[project.url, project.id] ),
                                ]:
                                return redirect('users:validate_token')  

                        if request.path in [
                             
                            reverse('users:signup'), 
                            reverse('users:update_profile'),
                            reverse('users:update_user'),
                            reverse('users:social_net'),
                            reverse('users:change_password'),
                            reverse('users:delete_user'),

                            reverse('posts:feed'),  
                            reverse('posts:list_project'), 
                            reverse('posts:new_project'),

                            reverse('iteractions:list_user'),
                            reverse('iteractions:notification'),
                            reverse('iteractions:send-direct'),
                            
                            ]:
                            return redirect('users:validate_token')
        response = self.get_response(request)
        return response


