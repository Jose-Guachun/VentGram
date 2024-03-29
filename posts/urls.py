#Postss Urls

#Django
from django.urls import path


#importaciones de apps
from posts import views

urlpatterns = [

    #managment

    path(
        route='',
        view=views.PostHomeView,
        name='home'
        ),
        
    path(
        route='posts/',
        view=views.ProjectFeedView,
        name='feed'
        ),

    path(
        route='posts/projects',
        view=views.FilterProjectView,
        name='list_project'
        ),

    path(
        route='posts/create_project',
        view=views.CreatedProjectView.as_view(),
        name='new_project'
        ), 

    path(
        route='posts/<slug:url>/project1<int:project_id>48/',
        view=views.ProjectDetailView,
        name='detail_project'
        ),

    path(
        route='update_project/<slug:url>/',
        view=views.UpdateProjectView.as_view(),
        name='update_project'
        ),

    path(
        route='delete_project/<slug:url>/',
        view=views.ProjectDeleteView.as_view(),
        name='delete_project'
    ),
        
]
