from .models import Blog, Post, Typer, Author,Comment
from rest_framework import serializers, generics, viewsets

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class TyperSerializers(serializers.ModelSerializer):
    class Meta:
        model = Typer
        fields = '__all__'


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'