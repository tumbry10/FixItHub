from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    #Category urls
    path('category/create/', views.create_category, name='create_category'),
    path('category/list/', views.list_category, name='list_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('category/update/<int:pk>/', views.update_category, name='update_category'),

    #issues urls
    path('issue/create/', views.create_issue, name='create_issue'),
    path('issue/list/', views.list_issue, name='list_issue'),
    path('issue/update/<int:pk>/', views.update_issue, name='update_issue'),
    path('issue/delete/<int:pk>/', views.delete_issue, name='delete_issue'),
]
