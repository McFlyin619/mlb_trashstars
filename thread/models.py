from django.db import models
import datetime
from django.template.defaultfilters import length, slugify
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class GameThread(models.Model):
    date = models.DateField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        self.slug = slugify('padres-' + str(self.date))
        super(GameThread, self).save(*args, **kwargs)

class Comment(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField(max_length=300, blank=True)
    thread = models.ForeignKey(GameThread, on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_like')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.by) + ' - ' + self.comment_body


