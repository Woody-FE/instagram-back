from articles.serializers import BaseFeedSerializer, UserInfoSerializer
from rest_framework import serializers
from .models import Notification
class NotificationSerializer(serializers.ModelSerializer):
    from_user = UserInfoSerializer()
    feed = BaseFeedSerializer()

    class Meta:
        model = Notification
        fields = '__all__'