from django.shortcuts import render
from rest_framework import viewsets
from ghostpost.serializers import PostSerializer
from ghostpost.models import Post
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    @action(detail=False)
    def get_boasts(self, request):
        boasts = Post.objects.filter(roast_or_boast=True)
        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def get_roasts(self, request):
        roasts = Post.objects.filter(roast_or_boast=False)
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def sort_posts(self, request):
        posts = Post.objects.all()
        sorted_posts = sorted(posts, key=lambda x: x.votetotal, reverse=True)
        serializer = self.get_serializer(sorted_posts, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=None):
        post_id = Post.objects.get(id=pk)
        post_id.up_vote += 1
        post_id.save()
        return Response({'status': 'ok'})
    
    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk=None):
        post_id = Post.objects.get(id=pk)
        post_id.down_vote -= 1
        post_id.save()
        return Response({'status': 'ok'})