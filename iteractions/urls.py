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

    path(
        route='<int:project_id>/<str:project_slug>/',
        view=views.like,
        name='like_project'
        ),

    path(
        route='<int:post_id>/favorite',
        view=views.favorite,
        name='post_favorite'
        ),
        
    path(
        route='notification/',
        view=views.ShowNOtifications,
        name='notification'
        ),
    
    path(
        route='<noti_id>/delete',
        view=views.DeleteNotification,
        name='delete-notification'),

    path(
        route='<int:comment>/<str:url>/delete',
        view=views.DeleteComments,
        name='delete-comments'),

     path(
        route='messages/',
        view=views.MessagesViews.as_view(),
        name='messages'
        ),
]











