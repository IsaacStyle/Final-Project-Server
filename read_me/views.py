from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import UserSerializer,PostSerializer,CommentsSerializer,SubsSerializer
from .models import User,Post,Subs,Comments

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    queryset = Subs.objects.all()
    serializer_class = SubsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer