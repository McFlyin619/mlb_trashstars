from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewSet, GameThreadListView, dislike_view,
                    gamethread_details, like_view, home, user_logout)

router = routers.DefaultRouter()
router.register('comments', CommentViewSet)

app_name = 'thread_app'

urlpatterns = [
    path('', home, name='home'),
    path('',include(router.urls)),
    path('game-threads/', GameThreadListView.as_view(), name='gamethread_list'),
    path('<int:pk>/', gamethread_details, name='gamethread_detail'),
    path('like/<int:pk>/<int:id>', like_view, name='like_comment'),
    path('dislike/<int:pk>/<int:id>', dislike_view, name='dislike_comment'),
    path('logged_out/',user_logout, name='user_logout'),
]
