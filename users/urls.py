#Users Urls

#Django
from django.urls import path


#importaciones de apps
from users import views

urlpatterns = [

    #managment
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login',
        ),

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup',
        ),
    
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
        ),

    path(
        route='mail/',
        view=views.email_verified,
        name='mail'
        ),    
]