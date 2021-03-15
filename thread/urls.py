from django.contrib import admin
from django.urls import path, include
from .views import HomeView, GameThreadListView, CommentViewSet, gamethread_details, like_view, dislike_view
from rest_framework import routers


router = routers.DefaultRouter()
router.register('comments', CommentViewSet)

app_name = 'thread_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('',include(router.urls)),
    path('game-threads/', GameThreadListView.as_view(), name='gamethread_list'),
    path('<int:pk>/', gamethread_details, name='gamethread_detail'),
    path('like/<int:pk>/<int:id>', like_view, name='like_comment'),
    path('dislike/<int:pk>/<int:id>', dislike_view, name='dislike_comment'),
]
