
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .models.blog_models import BlogPostModels
from .models.message import Message
from .models.member import Members
from .models.project import Projects
from .models.customer_comments import Customer_opinion
from .serializer import BlogSerializer,MessageSerializer,MemberSerializer,ProjectsSerializer,CustomerSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework.response import Response

from rest_framework.decorators import action,api_view
# Create your views here.

class PostCreateApiView(ListAPIView):
    queryset = BlogPostModels.objects.all()
    serializer_class = BlogSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# permissions.pydan  to'g'irlandi
    queryset = BlogPostModels.objects.all()
    serializer_class = BlogSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

#
class MembersViewset(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Members.objects.all()



class ProjectsViewset(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class CustomerCommentViews(viewsets.ModelViewSet):
    queryset = Customer_opinion.objects.all()
    serializer_class = CustomerSerializer
