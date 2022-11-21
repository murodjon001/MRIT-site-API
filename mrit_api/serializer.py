from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models.blog_models import BlogPostModels
from .models.message import Message
from .models.member import Members
from .models.project import Projects
from .models.customer_comments import Customer_opinion

from rest_framework.exceptions import ValidationError


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModels
        fields = ['id','author','title','text','photo','created_at',]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username',]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','name','email','phone','text',]

class MemberSerializer(serializers.ModelSerializer):

    youtube = serializers.URLField(source='telegram')
    class Meta:
        model = Members
        fields = ['full_name','image','youtube','instagram','facebook','linkidin','github']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id','project_name','images','project_url']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_opinion
        fields = ['id','client_fullname','identity','project','photo','comments',]