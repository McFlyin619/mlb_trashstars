import datetime

import statsapi
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from rest_framework import viewsets
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from thread.models import Comment, GameThread
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .models import *
from .serializers import CommentSerializer


# Create your views here.
def home(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    today = datetime.datetime.now()
    yesterday = datetime.datetime.now().day - 1
    last_game = statsapi.schedule(date=str(year) + "-" + str(month) +"-" + str(yesterday), team=135)
    next_game = statsapi.schedule(date=str(year) + "-" + str(month) +"-" + str(day), team=135)


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('thread_app:home'))

            else: 
                return HttpResponse('Account is not active!')
        
        else:
            print('someone tried to login unsuccessfully!')
            return HttpResponse('<h1 class="text-center">Username or Password does not match our records. Please try again.</h1>')

    else:
        context = {
        'last_game':last_game,
        'next_game':next_game,
        
    }
        return render(request, 'thread/home.html', context=context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('thread_app:home'))

# class HomeView(TemplateView):
#     template_name = 'thread/home.html'
#     year = datetime.datetime.now().year
#     month = datetime.datetime.now().month
#     day = datetime.datetime.now().day
#     today = datetime.datetime.now()
#     yesterday = datetime.datetime.now().day - 1
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         year = datetime.datetime.now().year
#         month = datetime.datetime.now().month
#         day = datetime.datetime.now().day
#         yesterday = datetime.datetime.now().day - 1
#         context["last_game"] = statsapi.schedule(date=str(year) + "-" + str(month) +"-" + str(yesterday), team=135)
#         context["next_game"] = statsapi.schedule(date=str(year) + "-" + str(month) +"-" + str(day), team=135)
        
#         return context

def like_view(request, id, pk):
    this_comment = get_object_or_404(Comment, pk=request.POST.get('comment_id'))
    if this_comment.dislikes.filter(id=request.user.id).exists():
        this_comment.dislikes.remove(request.user)
        this_comment.likes.add(request.user)
    else:
        this_comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('thread_app:gamethread_detail', args=[str(id)]))

def dislike_view(request, id, pk):
    this_comment = get_object_or_404(Comment, pk=request.POST.get('comment_id1'))
    if this_comment.likes.filter(id=request.user.id).exists():
        this_comment.likes.remove(request.user)
        this_comment.dislikes.add(request.user)
    else:
        this_comment.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('thread_app:gamethread_detail', args=[str(id)]))


def gamethread_details(request, pk):
    this_thread = GameThread.objects.get(pk=pk)  
    comments = Comment.objects.filter(thread=this_thread)
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
            return HttpResponseRedirect(reverse('thread_app:gamethread_detail', args=[str(pk)]))

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

