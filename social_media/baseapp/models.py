from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    #image=ImageField()
    bio = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.name


class Post(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    #num_stars = models.IntegerField()

    def __str__(self):
        #return self.writer
        return str(self.content)