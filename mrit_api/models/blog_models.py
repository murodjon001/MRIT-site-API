from django.db import models
from django.contrib.auth.models import User


class BlogPostModels(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=False,blank=False)
    text = models.TextField(null=False,blank=False)
    photo = models.ImageField(null=True,blank=True,upload_to='media/')
    created_at = models.DateField(null=True,blank=True,auto_now=True)
    updated_at = models.DateField(null=True,blank=True,auto_now=True)


    def __str__(self):
        return self.title