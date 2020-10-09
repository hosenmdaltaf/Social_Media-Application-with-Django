from django.db import models
from users.models import Profile


class Post(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    #num_stars = models.IntegerField()

    def __str__(self):
        #return self.writer
        return str(self.content)