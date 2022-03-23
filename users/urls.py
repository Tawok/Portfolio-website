from django.urls import path
from .views import (UserCreationView, 
                    UserLoginView, 
                    UserLogoutView, 
                    UserProfileView,
                    UpdateUserProfileView, 
                    UserSocialSitesView,
                    UserSocialSitesUpdateView,
                    UserSocialSitesDeleteView,
                    UserProjectsView,
                    UserProjectDetailView,
                    UserProjectDeleteView,
                    UserProjectUpdateView,
                )


app_name = 'users'
urlpatterns = [
    path('register/', UserCreationView.as_view(), name='create-user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', UpdateUserProfileView.as_view(), name='update-profile'),
    path('profile/<int:pk>/add-site/', UserSocialSitesView.as_view(), name = 'create-site'),
    path('profile/<int:pk>/update-site/', UserSocialSitesUpdateView.as_view(), name = 'update-site'),
    path('profile/<int:pk>/delete-site/', UserSocialSitesDeleteView.as_view(), name = 'delete-site'),
    path('profile/<int:pk>/add-project/', UserProjectsView.as_view(), name = 'create-project'),
    path('profile/<int:pk>/project-detail/', UserProjectDetailView.as_view(), name = 'project-detail'),
    path('profile/<int:pk>/project-delete/', UserProjectDeleteView.as_view(), name = 'project-delete'),
    path('profile/<int:pk>/project-update/', UserProjectUpdateView.as_view(), name = 'project-update')
]