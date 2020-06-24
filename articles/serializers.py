from django.contrib.auth import get_user_model
from .models import Feed, FeedImage, Comment, Tag
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

User = get_user_model()

# 댓글, 좋아요에 들어갈 간소화된 유저
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo')

# 피드에 들어갈 사진
class FeedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedImage
        fields = ('image',)
        
# 댓글 리스트
class FeedCommentSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at', 'updated_at')

# 간소화된 피드 ( 해당 유저의 피드 디테일로 들어가면 나오는 피드 )
class BaseFeedSerializer(serializers.ModelSerializer):
    images = FeedImageSerializer(source="feedimage_set", many=True, read_only=True)
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    class Meta:
        model = Feed
        fields = ('id', 'images', 'like_count', 'comment_count')

# 해당 유저의 피드 리스트 ( 간소화된 피드 리스트를 가짐 )
class UserFeedListSerializer(serializers.ModelSerializer):
    feed_set = BaseFeedSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo', 'feed_set')

# 기본 피드 리스트 ( 메인 페이지에서 보여주는 정보가 많음 )
class FeedSerializer(TaggitSerializer, serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    # 임시로 이미지를 막아둠 ( read_only 제거하면 사용 가능 )
    images = FeedImageSerializer(source="feedimage_set", many=True, read_only=True)
    like_users = UserInfoSerializer(many=True, read_only=True)
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    comments = FeedCommentSerializer(many=True, read_only=True)
    tags = TagListSerializerField()
    class Meta:
        model = Feed
        fields = ('id', 'user', 'content', 'images', 'comments', 'comment_count', 'tags', 'like_users', 'like_count','created_at', 'updated_at')

# 피드의 디테일 페이지
class FeedDetailSerializer(FeedSerializer):
    user = UserFeedListSerializer()