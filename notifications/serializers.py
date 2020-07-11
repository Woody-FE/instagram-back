from articles.serializers import SmallFeedSerializer, UserInfoSerializer
from rest_framework import serializers
from .models import Notification
class NotificationSerializer(serializers.ModelSerializer):
    from_user = UserInfoSerializer()
    to_user = UserInfoSerializer()
    feed = SmallFeedSerializer()

    class Meta:
        model = Notification
        fields = '__all__'