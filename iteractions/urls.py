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
            
    path(
        route='<int:project_id>/like',
        view=views.like,
        name='like_project'
        ),
        
    path(
        route='notification/',
        view=views.ShowNOtifications,
        name='notification'
        ),

     path(
        route='messages/',
        view=views.MessagesViews.as_view(),
        name='messages'
        ),
 
]











