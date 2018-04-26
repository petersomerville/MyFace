from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name = 'index'),

    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),

    path('search_users', views.search_users, name = 'search_users'),
    path('results/<str:term>', views.results, name = 'results'),

    path('follow/<int:following_id>', views.follow, name = 'follow'),
    path('unfollow/<int:following_id>', views.unfollow, name = 'unfollow'),
]