from django import forms
from django.forms.models import ModelForm
from .models import Comment
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_body',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['comment_body'].label = 'Is this an All-Star or Trash comment?'

