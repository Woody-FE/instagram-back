from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserFollowList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo')

class UserDetailSerializer(serializers.ModelSerializer):
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    followers = UserFollowList(many=True)
    followings = UserFollowList(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo', 'name', 'gender', 'description', 'followings', 'followers','followers_count', 'following_count',)

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_photo', 'name', 'gender', 'description')

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'profile_photo',
            'username',
            'name',
        )