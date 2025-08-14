from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

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

    #User edit & delete their own issue.
    path('issue_edit/<int:pk>/', views.edit_my_issue, name='edit_my_issue'),
    path('issue_delete/<int:pk>/', views.delete_my_issue, name='delete_my_issue'),
]
