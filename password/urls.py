from django.urls import path
from . import views

from password.views import UserListView, AuthLevelListView, AccountListView

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('user/', UserListView.as_view(), name='user-list'),
    path('authlevel/', AuthLevelListView.as_view(), name='auth-level-list'),
    path('account/', AccountListView.as_view(), name='account-list'),
]