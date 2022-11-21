from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=200,null=False,blank=False)
    images = models.ImageField(null=True,blank=True,upload_to=('media'))
    project_url = models.URLField(null=True,blank=True,max_length=200)

    def __str__(self):
        return self.project_name