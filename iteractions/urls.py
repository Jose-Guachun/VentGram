#Django
from django.urls import path


#importaciones de apps
from iteractions import views


urlpatterns = [
        
    path(
        route='follow/<str:username>/<str:project_slug>/',
        view=views.follow,
        name='follow',
        ),

    path(
        route='unfollow/<str:username>/<str:project_slug>/',
        view=views.unfollow,
        name='unfollow',
        ),

    path(
        route='list_user/',
        view=views.UserListView,
        name='list_user',
        ),
]











