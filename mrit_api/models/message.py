from django.db import models


class Message(models.Model):
    name = models.CharField(null=False,blank=False,max_length=30)
    email = models.CharField(null=True,blank=True,max_length=100)
    phone = models.CharField(null=False,blank=False,max_length=13)
    text = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.name

