from django import forms
<<<<<<< HEAD
from .models import Comment

=======
from django.forms.models import ModelForm
from .models import Comment
>>>>>>> c5dea2d6b386476082e91d0bb038a99bff0730a7
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_body',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
<<<<<<< HEAD
        self.fields['comment_body'].label = 'Is this an All-Star or Trash comment?'
=======
        self.fields['comment_body'].label = 'Is this an All-Star or Trash comment?'

>>>>>>> c5dea2d6b386476082e91d0bb038a99bff0730a7
