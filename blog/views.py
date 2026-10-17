from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse # reverse allows us to create a url from a url pattern name
from .models import Article, Comment
from .forms import CreateArticleForm, CreateCommentForm, UpdateArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin ## for authentication
from django.contrib.auth.forms import UserCreationForm ## for new user
from django.contrib.auth.models import User ## the Django user model 

import random

# Create your views here.
class ShowAllView(ListView):
    '''define a view class to show all blog Articles'''
    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles"

    def dispatch(self, request, *args, **kwargs):
        '''override the dispatch method to add debugging info'''
        if request.user.is_authenticated:
            print(f'ShowAllView.dispatch(): request.user={request.user}')
        else:
            print(f'ShowAllView.dispatch(): not logged in.')

        return super().dispatch(request, *args, **kwargs)

class ArticleView(DetailView):
    '''display a single article'''
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"
 
class RandomArticleView(DetailView):
    '''display a single article selected at random'''
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"

    # custom methods
    def get_object(self):
        '''return one intance of the Article object selected at random'''
        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        
        return article

class CreateArticleView(LoginRequiredMixin, CreateView):
    '''a view to handle creation of a new Article
    (1) display the HTML form to the user
    (2) process the form submission and store the new Article object (POST)'''
    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"

    def get_login_url(self):
        '''return the URL for this app's login page'''

        return reverse('login')
    
    def form_valid(self, form):
        # print out the form data
        print(f'CreateArticleView.form_valid(): {form.cleaned_data}')

        # find the logged in user
        user = self.request.user 
        print(f'CreateArticle.View.form_valid(): {user}')
        # attach that user to the form instance (to the Article object)
        form.instance.user = user 

        # delegate work to the superclass to do the rest
        return super().form_valid(form)

class CreateCommentView(CreateView):
    '''a view to handle creation of a new Comment on an Article'''
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    def get_success_url(self):
        '''provide a URL to redirect to after successfully creating a comment'''
        # return reverse('show_all') <- not elegant version

        pk = self.kwargs['pk']
        # call reverse to generate the URL

        return reverse('article', kwargs={'pk': pk})

    def get_context_data(self):
        '''return the dictionary of context variables for use in the template'''

        # calling the superclass method
        context = super().get_context_data()
        # find/add the article to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        # add this article into the context dict
        context['article'] = article

        return context

    def form_valid(self, form):
        '''this method handles the form submission and saves the new object to the Django database.
        we need to add the FK (of the Article) to the Comment object before saving it to the database.'''
        
        print(form.cleaned_data) # for debugging purpose

        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        # attach this article to the comment
        form.instance.article = article # set the FK <- purpose for overriding superclass's form_valid!

        # delegate the work to the superclass method form_valid
        return super().form_valid(form)

class UpdateArticleView(UpdateView):
    '''view class to handle update of an article based on its PK'''

    model = Article
    form_class = UpdateArticleForm 
    template_name = "blog/update_article_form.html"

class DeleteCommentView(DeleteView):
    '''view class to delete a comment on an Article'''

    model = Comment
    template_name = "blog/delete_comment_form.html"

    def get_success_url(self):
        '''return the URL to redirect to after a successful delete'''

        # find the PK for this Comment
        pk = self.kwargs['pk']
        # find the Comment object
        comment = Comment.objects.get(pk=pk)
        # find the PK of the Article to which this commetn is associated
        article = comment.article

        return reverse('article', kwargs={'pk': article.pk})

class UserRegistrationView(CreateView):
    '''a view to show/process the registration form to create a new User'''
    model = User
    form_class = UserCreationForm
    template_name = "blog/register.html"

    def get_success_url(self):
        '''the URL to redirect to after creating a new User'''

        return reverse('login')

