from django.urls import path
from . views import PostCreateApiView,PostDetail,MessageViewSet,MembersViewset,ProjectsViewset,CustomerCommentViews
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'message',MessageViewSet)
router.register(r'members',MembersViewset)
router.register(r'projects',ProjectsViewset)
router.register(r"comments",CustomerCommentViews)

urlpatterns =[
    path('post/', PostCreateApiView.as_view()),
    path("post/<int:pk>/",PostDetail.as_view()),


]+router.urls



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

