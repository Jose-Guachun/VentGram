#Postss Urls

#Django
from django.urls import path


#importaciones de apps
from posts import views

urlpatterns = [

    #managment
    path(
        route='',
        view=views.PostHomeView.as_view(),
        name='home'
        ),
        
    path(
        route='posts/feed',
        view=views.PostFeedView.as_view(),
        name='feed'
        ),
        
]
