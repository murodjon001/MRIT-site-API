from django.db import models



class Customer_opinion(models.Model):
    client_fullname = models.CharField(max_length=150,null=False,blank=False)
    identity = models.CharField(max_length=79,null=False,blank=False)
    project = models.URLField(max_length=250,null=True,blank=True)
    photo = models.ImageField(null=True,blank=True,upload_to='media')
    comments = models.TextField(null=False, blank=False)


    def __str__(self):
        return self.client_fullname

