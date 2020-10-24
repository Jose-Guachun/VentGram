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
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout',
        ),

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup',
        ),
    
    path(
        route='me/update_profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
        ),

    path(
        route='me/add_social_net/',
        view=views.UpdateSocialNet.as_view(),
        name='social_net'
        ),

    path(
        route='me/update_user/',
        view=views.UpdateUserView.as_view(),
        name='update_user'
        ),
        
    path(
        route='me/update_password/', 
        view=views.UserChangePasswordView.as_view(),
        name='change_password'
        ),

    path(
        route='me/delete_account/', 
        view=views.UserDelete.as_view(),
        name='delete_user'
        ),

    path(
        route='mail/',
        view=views.email_verified,
        name='mail'
        ),

    #profile
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
   
    #Ajax
    path(
        route='ajax/provinces/',
        view=views.load_province,
        name='ajax_load_province'
    ),

        path(
        route='ajax/city/',
        view=views.load_city,
        name='ajax_load_city'
    ),

]