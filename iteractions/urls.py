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
        route='<int:post_id>/<int:position>',
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
        name='delete-notification'
        ),

    path(
        route='<int:comment_id>/<str:url>/delete',
        view=views.DeleteComments,
        name='delete-comments'
        ),

    path(
        route='messages/<str:username>',
        view=views.Inbox,
        name='messages'
        ),

    path(
        route='messages/directs/<username>',
        view=views.Directs,
        name='directs'
        ),

    path(
        route='messages/send/',
        view=views.SendDirect, 
        name='send-direct'
        ),

    path(
        route='messages/new/<username>',
        view=views.NewConversation, 
        name='newconversation'
        ),

    path(
        route='delete/<recipient>',
        view=views.DeleteConversation, 
        name='delete_conversation'
        ),

]











