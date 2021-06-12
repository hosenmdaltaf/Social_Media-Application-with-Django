
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
    title = models.CharField(max_length=200,null=True,blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    # post_date = models.DateField(auto_now_add=True)
    post_updated = models.DateField(auto_now=True)
    image=models.ImageField(upload_to='post_images', blank=True, null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True, blank=True)

#     rating = models.IntegerField()
#     security=
#    comment
#    share
    view_count=models.IntegerField(default=0)
   # slug=models.SlugField(blank=True,unique=True)

    def __str__(self):
        #return self.writer
        return str(self.writer) + '---' + str(self.title)

    def get_absolute_url(self,id):
        return reverse('baseapp:articale-detail',kwargs={'id':self.id})

      
  

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
   

    def __str__(self):
        return self.name

    


class Comment(models.Model):
    post = models.ForeignKey('baseapp.Post', on_delete=models.CASCADE, related_name='comments')
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

        




