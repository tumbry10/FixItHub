from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_syst_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/update/', views.update_user_profile, name='update_user_profile'),
    path('profile/', views.view_user_profile, name='view_user_profile'),
]
