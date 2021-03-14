from django.contrib import admin
from django.urls import path, include
from .views import GameThreadDetailView, HomeView, GameThreadListView, CommentViewSet, gamethread_details
from rest_framework import routers


router = routers.DefaultRouter()
router.register('comments', CommentViewSet)

app_name = 'thread_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('',include(router.urls)),
    path('game-threads/', GameThreadListView.as_view(), name='gamethread_list'),
    # path('<slug:slug>/', GameThreadDetailView.as_view(), name='gamethread_detail'),
    path('<slug:slug>/', gamethread_details, name='gamethread_detail'),
]
