from django.shortcuts import render
from rest_framework import viewsets, generics, generics,permissions
# Create your views here.
from .serializers import BlogSerializers, TyperSerializers, AuthorSerializers, PostSerializers,CommentSerializers
from .models import Blog, Post, Typer, Author, Comment
from rest_framework.authentication import TokenAuthentication

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = TokenAuthentication

    def get_queryset(self):
        return Blog.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    permission_classes = [permissions.DjangoModelPermissions]
    def get_queryset(self):
        return Post.objects.all()


class TyperViewSet(viewsets.ModelViewSet):
    serializer_class = TyperSerializers
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Typer.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    permission_classes = [permissions.DjangoModelPermissions]


    def get_queryset(self):
        return Post.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializers
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


    def get_queryset(self):
        return Author.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = TokenAuthentication

    def get_queryset(self):
        return Comment.objects.all()