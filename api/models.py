from thread.models import GameThread
from django.db import models
from tastypie.resources import ModelResource, ALL, fields
from tastypie.authorization import Authorization
from thread.models import GameThread, Comment
# Create your models here.

class ThreadResource(ModelResource):
    class Meta:
        queryset = GameThread.objects.all()
        resource_name = 'threads'
        ordering = ['date']
        
class CommentResource(ModelResource):
    thread = fields.ToOneField(ThreadResource,'game_thread', full=True)
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        ordering = ['date']
        allowed_methods = ['get','post','patch','put','delete','options'] #allows api to create to post
        authorization = Authorization()  # authorize all requests to have write db permissions