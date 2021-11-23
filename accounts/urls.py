from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('api-token-auth/', obtain_jwt_token),
    path('getuserlist/', views.getuserlist),
    
    
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('<username>/', views.profile, name='profile'),
    # path('<int:user_pk>/follow/', views.follow, name='follow'),    
]
