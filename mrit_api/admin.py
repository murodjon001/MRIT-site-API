from django.contrib import admin
from .models.blog_models import BlogPostModels
from .models.message import Message
from .models.member import Members
from .models.project import Projects
from .models.customer_comments import Customer_opinion

# Register your models here.


admin.site.register(BlogPostModels)
admin.site.register(Message)
admin.site.register(Members)
admin.site.register(Projects)
admin.site.register(Customer_opinion)



