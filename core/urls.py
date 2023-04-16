from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('user/', views.user_list, name='user_list'), #url ok views ok
    path('project/', views.project_list, name='project_list'), #url ok views ok
    path('user_project/associate/', views.user_project_associate, name='user_project_associate'), #url ok views ok
    path('project/create/', views.project_create, name='project_create'), #url ok views ok
    path('user/create/', views.user_create, name='user_create'),# url ok views ok
    path('project/edit/<int:id>/', views.edit_project, name='edit_project'), #url ok views ok


    # API URLs
    path('api/user/list/', views.UserListAPIView.as_view(), name='api_user_list'),
    path('api/user/search/', views.UserSearchAPIView.as_view(), name='api_user_search'),
    path('api/project/list/', views.ProjectListAPIView.as_view(), name='api_project_list'),
    path('api/project/search/', views.ProjectSearchAPIView.as_view(), name='api_project_search'),
]
