
from django.db import models
from django.conf import settings

from django.db.models.signals import pre_save,post_delete
from django.conf import settings
from django.utils.text import slugify
from django.dispatch import receiver
from django.urls import reverse



# from django.contrib.auth.models import User
# from account.models import Account


class Post(models.Model):

    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField( blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateField(auto_now=True)
    image=models.ImageField(upload_to='post_images', blank=True, null=True)
  
#    comment
#    share
    view_count=models.IntegerField(default=0)
   # slug=models.SlugField(blank=True,unique=True)

    def __str__(self):
        #return self.writer
        return str(self.writer)
    class Meta:
        ordering = ['-post_date'] 

    def get_absolute_url(self,id):
        return reverse('posts:articale-detail',kwargs={'id':self.id})




class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True )
    created_date = models.DateTimeField(auto_now_add=True)
    # approved_comment = models.BooleanField(default=True)

    objects = models.Manager()

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def __str__(self):
        return str(self.created_by)

    def all_comments(self):
        return self.comment_set.all()

    @property
    def totat_comments_count(self):
        return self.comment_set.all().count()

        





