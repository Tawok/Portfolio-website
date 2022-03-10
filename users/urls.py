from django.urls import path
from .views import (UserCreationView, 
                    UserLoginView, 
                    UserLogoutView, 
                    UserProfileView, 
                    UserSocialSitesView,
                    UpdateUserProfileView
                )


app_name = 'users'
urlpatterns = [
    path('register/', UserCreationView.as_view(), name='create-user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', UpdateUserProfileView.as_view(), name='update-profile'),
    path('profile/<int:pk>/add-site/', UserSocialSitesView.as_view(), name = 'social')
]