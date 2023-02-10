from rest_framework import serializers
from .models import User,Subs,Post,Comments

class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subs
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

