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

    path('post', views.post, name='post'),
    path('return_posts/<str:posting>', views.return_posts, name='return_posts'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]