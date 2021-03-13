from thread.models import Comment, GameThread
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
import datetime
import statsapi
from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import *

# Create your views here.
class HomeView(TemplateView):
    template_name = 'thread/home.html'

class GameThreadListView(ListView):
    model = GameThread
    context_object_name = 'gamethreads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        today = datetime.datetime.now()

        game_thread, created = GameThread.objects.get_or_create(date=today)
        game_thread.value = self.request.POST.get(today)
        game_thread.save()
        context['next_game'] = statsapi.schedule(date=str(year) + "-" + str(month) +"-" + str(day), team=135)
        return context
    
class GameThreadDetailView(DetailView):
    model = GameThread
    context_object_name = 'gamethread'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(thread=self.get_object().id)
        context["this_game"] = statsapi.schedule(date=self.get_object().date, team=135)
        return context
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
