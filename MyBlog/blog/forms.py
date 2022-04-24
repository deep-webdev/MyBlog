from dataclasses import fields
from xml.etree.ElementTree import Comment
from django import forms
from blog.models import Post, Comments

class PostForm(forms.ModelForm):
    
    class meta():
        model = Post
        fields = ('author', 'title', 'text')
        
        # for styling of field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }
        
class CommentClass(forms.ModelForm):

    class meta():
        model = Comment
        fields = ('author', 'text')
        
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }