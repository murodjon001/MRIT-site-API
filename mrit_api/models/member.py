from django.db import models


class Members(models.Model):
    full_name = models.CharField(null=False,blank=False, max_length=70)
    image = models.ImageField(null=True,blank=True,upload_to='media/photo_member')
    telegram = models.CharField(max_length=200)
    instagram = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    linkidin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)

    def __str__(self):
        return self.full_name