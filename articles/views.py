from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth import get_user_model
from django.http import Http404
from accounts.permissions import IsOwnerOrReadOnly
from .serializers import FeedSerializer, FeedDetailSerializer, FeedCommentSerializer
from accounts.serializers import UserListSerializer
from .models import Feed, Comment, FeedImage
class FeedList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, format=None):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FeedSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class FeedDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, feed_pk):
        try:
            feed = Feed.objects.get(pk=feed_pk)
            # check_object_permissions가 없으면 APIView에서는 IsOwnerOrReadOnly가 작동하지 않음
            self.check_object_permissions(self.request, feed)
            return feed
        except Feed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, feed_pk, format=None):
        feed = self.get_object(feed_pk)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data)

    def put(self, request, feed_pk, format=None):
        feed = self.get_object(feed_pk)
        serializer = FeedDetailSerializer(feed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, feed_pk, format=None):
        feed = self.get_object(feed_pk)
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FeedCommentList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, feed_pk):
        try:
            return Feed.objects.get(pk=feed_pk)
        except Feed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, feed_pk):
        feed = self.get_object(feed_pk)
        comments = feed.comments.all()
        serializer = FeedCommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, feed_pk):
        serializer = FeedCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(feed_id=feed_pk, user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedCommentDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, feed_pk, comment_pk):
        try:
            comment = Comment.objects.get(pk=comment_pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, feed_pk, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = FeedCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, feed_pk, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FeedLike(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, feed_pk):
        try:
            return Feed.objects.get(pk=feed_pk)
        except Feed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request, feed_pk, format=None):
        feed = self.get_object(feed_pk)
        if feed.like_users.filter(id=request.user.id).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        feed.like_users.add(request.user)
        return Response(status=status.HTTP_200_OK)

class FeedUnLike(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, feed_pk):
        try:
            return Feed.objects.get(pk=feed_pk)
        except Feed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request, feed_pk, format=None):
        feed = self.get_object(feed_pk)
        if feed.like_users.filter(id=request.user.id).exists():
            feed.like_users.remove(request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class FeedLikeUsers(APIView):
    def get_object(self, feed_pk):
        try:
            return Feed.objects.get(pk=feed_pk)
        except Feed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, feed_pk, format=None):
        feed = self.get_object(feed_pk)
        feed_like_users = feed.like_users.all()
        serializer = UserListSerializer(feed_like_users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)