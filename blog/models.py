from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    '''Encapsulate the data of a blog Article by an author'''
    # define the data attributes of the Article object
    title = models.TextField(blank=True)
    author = models.TextField(blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        '''return the URL to display one instance of this model'''
        return reverse('article', kwargs={'pk': self.pk})

    def get_all_comments(self):
        '''return a QuerySet of comments about this article'''
        comments = Comment.objects.filter(article=self)

        return comments

class Comment(models.Model):
    '''encapsulate the idea of a Comment about an Article'''

    article = models.ForeignKey(Article, on_delete=models.CASCADE) # on_delete in case when FK for Article is deleted; CASCADE deletes all of the comments on that article
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text}'
