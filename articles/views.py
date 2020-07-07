from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth import get_user_model
from django.http import Http404
from accounts.permissions import IsOwnerOrReadOnly
from .serializers import FeedSerializer, FeedDetailSerializer, FeedCommentSerializer, SmallFeedSerializer, UserInfoSerializer
from accounts.serializers import UserListSerializer
from .models import Feed, Comment, FeedImage
from notifications.views import notification_create
from django.db.models import Q

class FeedList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, format=None):
        # feeds = Feed.objects.all()
        # request user의 팔로우 유저 등의 피드를 제공하도록 로직 구성 생각중
        if request.user.pk == None:
            feeds = Feed.objects.all().order_by('-created_at')
        else:
            feeds = []
            follower_users = request.user.followers.all()
            for follower_user in follower_users:
                if follower_user.is_private == True:
                    if not follower_user.followings.filter(pk=request.user.pk).exists():
                        continue
                follower_feeds = follower_user.feed_set.all().order_by('-created_at')[:5]
                feeds.extend(follower_feeds)
            my_feeds = request.user.feed_set.all().order_by('-created_at')[:5]
            feeds.extend(my_feeds)
            feeds.sort(key=lambda feed: feed.created_at, reverse=True)
                
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
        if feed.user.is_private == True:
            if not feed.user.followers.filter(pk=request.user.pk).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data)

    def put(self, request, feed_pk, format=None):
        feed = self.get_object(feed_pk)
        serializer = FeedDetailSerializer(feed, data=request.data)
        if serializer.is_valid(raise_exception=True):
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
        feed = self.get_object(feed_pk)
        serializer = FeedCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(feed_id=feed.id, user=request.user)
            notification_create(request.user, feed.user, 'comment', feed, serializer.data['content'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedCommentDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, comment_pk):
        try:
            comment = Comment.objects.get(pk=comment_pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, feed_pk, comment_pk, format=None):
        comment = self.get_object(comment_pk)
        serializer = FeedCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, feed_pk, comment_pk, format=None):
        comment = self.get_object(comment_pk)
        serializer = FeedCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, feed_pk, comment_pk, format=None):
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
        notification_create(request.user, feed.user, 'like', feed)
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

class FeedCommentLike(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, comment_pk):
        try:
            return Comment.objects.get(pk=comment_pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request, feed_pk, comment_pk, format=None):
        comment = self.get_object(comment_pk)
        if comment.like_users.filter(id=request.user.id).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        comment.like_users.add(request.user)
        notification_create(request.user, comment.user, 'like', None, comment.content)
        return Response(status=status.HTTP_200_OK)

class FeedCommentUnLike(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, comment_pk):
        try:
            return Comment.objects.get(pk=comment_pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request, feed_pk, comment_pk, format=None):
        comment = self.get_object(comment_pk)
        if comment.like_users.filter(id=request.user.id).exists():
            comment.like_users.remove(request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class FeedLikeUsers(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get_object(self, feed_pk):
#         try:
#             return Feed.objects.get(pk=feed_pk)
#         except Feed.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, feed_pk, format=None):
#         feed = self.get_object(feed_pk)
#         feed_like_users = feed.like_users.all()
#         serializer = UserListSerializer(feed_like_users, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


class Search(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        search = request.query_params.get('search', None)
        # 검색어가 비어있지않음
        if search != None:
            #태그일 경우
            if search[0] == '#':
                search = search[1:]
                feeds = Feed.objects.filter(tags__name__contains=search).order_by('-created_at').distinct()
                serializer = SmallFeedSerializer(feeds, many=True)
                return Response(serializer.data)
            #태그가 아닐 경우
            else:
                User = get_user_model()
                users = User.objects.filter(Q(name__contains=search) | Q(username__contains=search)).distinct()
                serializer = UserInfoSerializer(users, many=True)
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
