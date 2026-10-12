# define the forms that we use for create/update/delete operations

from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):
    '''a form to add an Article to the database'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Article
        # fields = ['author', 'title', 'text', 'image_url']
        fields = ['author', 'title', 'text', 'image_file']

class CreateCommentForm(forms.ModelForm):
    '''a form to add an Comment to the database'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Comment
        fields = ['author', 'text']

class UpdateArticleForm(forms.ModelForm):
    '''a form to handle an update to an Article'''

    class Meta:
        model = Article 
        fields = ['title', 'text']
