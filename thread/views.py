from thread.models import Comment, GameThread
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
import datetime
import statsapi
from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import *
from .forms import CommentForm
from django.db.models import Count
from django.http import HttpResponseRedirect
# Create your views here.
class HomeView(TemplateView):
    template_name = 'thread/home.html'

def like_view(request, id, pk):
    this_comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    if this_comment.dislikes.filter(id=request.user.id).exists():
        this_comment.dislikes.remove(request.user)
        this_comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('thread_app:gamethread_detail', args=[str(id)]))

def dislike_view(request, id, pk):
    this_comment = get_object_or_404(Comment, id=request.POST.get('comment_id1'))
    if this_comment.likes.filter(id=request.user.id).exists():
        this_comment.likes.remove(request.user)
        this_comment.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('thread_app:gamethread_detail', args=[str(id)]))


def gamethread_details(request, pk):
    this_thread = GameThread.objects.get(pk=pk)  
    comments = Comment.objects.filter(thread=this_thread)[:30]
    comment_count = Comment.objects.filter(thread=this_thread).count()
    this_game = statsapi.schedule(date=this_thread, team=135)
    
    if request.method == 'POST':
        form = CommentForm(data=request.POST)

        if form.is_valid():
            if 'comment_body' in request.POST:
                comment_form = form.save(commit=False)
                comment_form.by = request.user
                comment_form.thread = this_thread

                comment_form.save()
                form = CommentForm()

        else:
            print(form.errors)
        
    else:
        form = CommentForm()
       

    context = {
        'this_game':this_game,
        'comments':comments,
        'comment_count':comment_count,
        'comment_form':form,
        'this_thread':this_thread,
        
    }
    return render(request,'thread/gamethread_detail.html', context=context)

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
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
