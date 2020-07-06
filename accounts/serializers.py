from django.contrib.auth import get_user_model
from rest_framework import serializers
from articles.serializers import SmallFeedSerializer

User = get_user_model()

class UserFollowList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo')

class UserDetailSerializer(serializers.ModelSerializer):
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    followers = UserFollowList(many=True, read_only=True)
    followings = UserFollowList(many=True, read_only=True)
    feed_set = SmallFeedSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo', 'name', 'gender', 'description', 'followings', 'followers', 'followers_count', 'following_count', 'feed_set')

# class UserProfileUpdateSerializer(UserDetailSerializer):
#     class Meta(UserDetailSerializer.Meta):
        # model = User
        # fields = ('id', 'username', 'profile_photo', 'name', 'gender', 'description')

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'profile_photo',
            'username',
            'name',
        )