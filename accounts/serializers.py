from django.contrib.auth import get_user_model
from rest_framework import serializers
from articles.serializers import SmallFeedSerializer

User = get_user_model()

class UserFollowList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo')

class PrivateUserDetailSerializer(serializers.ModelSerializer):
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    followers = UserFollowList(many=True, read_only=True)
    followings = UserFollowList(many=True, read_only=True)
    private_user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo', 'name', 'gender', 'description', 'followings', 'followers', 'followers_count', 'following_count', 'is_private', 'private_user')

    def get_private_user(self, obj):
        return True

class UserDetailSerializer(PrivateUserDetailSerializer):
    feed_set = SmallFeedSerializer(many=True, read_only=True)

    class Meta(PrivateUserDetailSerializer.Meta):
        fields = ('id', 'username', 'profile_photo', 'name', 'gender', 'description', 'followings', 'followers', 'followers_count', 'following_count', 'is_private', 'feed_set', 'private_user')

    def get_private_user(self, obj):
        return False
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