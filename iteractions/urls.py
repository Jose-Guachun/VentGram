#Django
from django.urls import path


#importaciones de apps
from iteractions import views


urlpatterns = [
    path(
        route='follow/<str:username>/',
        view=views.follow,
        name='follow',
        ),

	path(
        route='unfollow/<str:username>/',
        view=views.unfollow,
        name='unfollow',),
        
]











