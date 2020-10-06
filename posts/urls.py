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
        view=views.ProjectFeedView.as_view(),
        name='feed'
        ),

    path(
        route='posts/<int:pk>/',
        view=views.ProjectDetailView.as_view(),
        name='detail_project'
        ),

    path(
        route='posts/new_project',
        view=views.CreatedProjectView.as_view(),
        name='new_project'
        ), 

    path(
        route='posts/project',
        view=views.PostProjectView.as_view(),
        name='project'
        ),
        
]
