from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from django.http import Http404
from .serializers import UserDetailSerializer, UserListSerializer #UserProfileUpdateSerializer
from .permissions import IsOwnerOrReadOnly, IsMineOrReadOnly
from rest_framework.permissions import IsAuthenticated
from notifications.views import notification_create

User = get_user_model()

# Create your views here.
class UserDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsMineOrReadOnly]
    def get_object(self, username):
        try:
            user = User.objects.get(username=username)
            self.check_object_permissions(self.request, user)
            return user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # 유저 조회
    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, username, format=None):
        user = self.get_object(username)
        # 수정 가능한 필드 name, gender, profile_photo, description
        # serializer = UserProfileUpdateSerializer(user, data=request.data, partial=True)
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None): 
        user = self.get_object(username)
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Follow(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, username, format=None):
        # if request.user.followings.filter(username=username).exists():
        user = self.get_object(username)
        if user != request.user:
            request.user.followings.add(user)
            notification_create(request.user, user, 'follow')
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UnFollow(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, username, format=None):
        # if request.user.followings.filter(username=username).exists():
        user = self.get_object(username)
        if user != request.user:
            request.user.followings.remove(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class UserFollowers(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get_object(self, username):
#         try:
#             return User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, username, format=None):
#         user = self.get_object(username)
#         user_followers = user.followers.all()
#         serializer = UserListSerializer(user_followers, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

# class UserFollowings(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get_object(self, username):
#         try:
#             return User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, username, format=None):
#         user = self.get_object(username)
#         user_followings = user.followings.all()
#         serializer = UserListSerializer(user_followings, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


