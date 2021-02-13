
from django.db import models
from django.conf import settings

from django.db.models.signals import pre_save,post_delete
from django.conf import settings
from django.utils.text import slugify
from django.dispatch import receiver




class Post(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
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

      
    def get_cat_list(self):
            k = self.category # for now ignore this instance method
            
            breadcrumb = ["dummy"]
            while k is not None:
                breadcrumb.append(k.slug)
                k = k.parent
            for i in range(len(breadcrumb)-1):
                breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
            return breadcrumb[-1:0:-1]
    '''
    @receiver(post_delete, sender=Post)
    def submission_delete(sender,instance, **kwargs):
        instance.image.delete(False)

    def pre_save_blog_post_receiver(sender,instance,*args, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.writer.username + "-" + instance.title)
    pre_save.connect(pre_save_blog_post_receiver,sender=Post)

     '''

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True, null=True ,related_name='children')

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])



class Comment(models.Model):
    post = models.ForeignKey('baseapp.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

        




