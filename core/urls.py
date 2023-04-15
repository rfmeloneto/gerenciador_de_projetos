from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('user/add/', views.user_add, name='user_add'),
    path('user/', views.user_list, name='user_list'),
    path('project/add/', views.project_add, name='project_add'),
    path('project/', views.project_list, name='project_list'),
    path('user_project/associate/', views.user_project_associate, name='user_project_associate'),
    path('project/create/', views.project_create, name='project_create'),
    path('user/create/', views.user_create, name='user_create'),


    # API URLs
    path('api/user/list/', views.UserListAPIView.as_view(), name='api_user_list'),
    path('api/user/search/', views.UserSearchAPIView.as_view(), name='api_user_search'),
    path('api/user/create/', views.UserCreateAPIView.as_view(), name='api_user_create'),
    path('api/user/<int:pk>/', views.UserDetailAPIView.as_view(), name='api_user_detail'),
    path('api/user_project/associate/', views.UserProjectAssociateAPIView.as_view(), name='api_user_project_associate'),
    path('api/user_project/disassociate/', views.UserProjectDisassociateAPIView.as_view(), name='api_user_project_disassociate'),
    path('api/project/list/', views.ProjectListAPIView.as_view(), name='api_project_list'),
    path('api/project/search/', views.ProjectSearchAPIView.as_view(), name='api_project_search'),
    path('api/project/create/', views.ProjectCreateAPIView.as_view(), name='api_project_create'),
    path('api/project/<int:pk>/', views.ProjectDetailAPIView.as_view(), name='api_project_detail'),
]
