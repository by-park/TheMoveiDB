from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=140)
    class Meta:
        model = Comment
        fields = ['content']
