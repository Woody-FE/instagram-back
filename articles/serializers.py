from django.contrib.auth import get_user_model
from .models import Feed, FeedImage, Comment, Tag
from rest_framework import serializers
import re

User = get_user_model()

# 태그
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

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
    like_users = UserInfoSerializer(many=True, read_only=True)
    comment_like_count = serializers.ReadOnlyField()
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'like_users', 'comment_like_count', 'created_at', 'updated_at')

# 간소화된 피드 ( 해당 유저의 피드 디테일로 들어가면 나오는 피드 )
class SmallFeedSerializer(serializers.ModelSerializer):
    images = FeedImageSerializer(source="feedimage_set", many=True, read_only=True)
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    class Meta:
        model = Feed
        fields = ('id', 'images', 'like_count', 'comment_count')

# 해당 유저의 피드 리스트 ( 간소화된 피드 리스트를 가짐 )
class UserFeedListSerializer(serializers.ModelSerializer):
    feed_set = SmallFeedSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_photo', 'followers', 'feed_set')

# 기본 피드 리스트 ( 메인 페이지에서 보여주는 정보가 많음 )
class FeedSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    images = FeedImageSerializer(source="feedimage_set", many=True, read_only=True)
    like_users = UserInfoSerializer(many=True, read_only=True)
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    comments = FeedCommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    def create(self, validated_data):
        # print(self.context.get('request').FILES)
        instance = super(FeedSerializer, self).create(validated_data)
        content = validated_data['content']
        tag_sets = re.findall(r'#(\w+)\b', content)
        ins_tags = []
        if tag_sets:
            for t in tag_sets:
                tag, tag_created = Tag.objects.get_or_create(name=t)
                instance.tags.add(tag)
        images_data = self.context['request'].FILES
        for image_data in images_data.getlist('image'):
            FeedImage.objects.create(user=instance.user, feed=instance, image=image_data)
        return instance

    class Meta:
        model = Feed
        fields = ('id', 'user', 'content', 'images', 'comments', 'comment_count', 'tags', 'like_users', 'like_count','created_at', 'updated_at')

# 피드의 디테일 페이지
class FeedDetailSerializer(FeedSerializer):
    user = UserFeedListSerializer(read_only=True)

    def update(self, instance, validated_data):
        if instance.content != validated_data.get('content'):
            instance.tags.clear()
            instance.content = validated_data.get('content', instance.content)
            tag_sets = re.findall(r'#(\w+)\b', instance.content)
            ins_tags = []
            if tag_sets:
                for t in tag_sets:
                    tag, tag_created = Tag.objects.get_or_create(name=t)
                    instance.tags.add(tag)
        instance.save()
        return instance
