from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f'{self.user.name} Profile'


    def __str__(self):
        return self.name
