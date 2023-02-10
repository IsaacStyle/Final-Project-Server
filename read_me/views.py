from rest_framework import viewsets

from .serializers import UserSerializer,PostSerializer,CommentsSerializer,SubsSerializer
from .models import User,Post,Subs,Comments

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubsViewSet(viewsets.ModelViewSet):
    queryset = Subs.objects.all()
    serializer_class = SubsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer