from django.urls import path
from . import views

from password.views import (
    UserListView, 
    AuthLevelListView, 
    AccountListView,
    UserDetailView, 
    AuthLevelDetailView,
    AccountDetailView
)

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('user/', views.UserListView.as_view(), name='user-list'),
    path('authlevel/', views.AuthLevelListView.as_view(), name='auth-level-list'),
    path('account/', views.AccountListView.as_view(), name='account-list'),
]

urlpatterns += [
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('authlevel/<int:pk>', views.AuthLevelDetailView.as_view(), name='auth-level-detail'),
    path('account/<int:pk>', views.AccountDetailView.as_view(), name='account-detail'),
]