from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer
# Create your views here.
class NotificationList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        notifications = Notification.objects.filter(to_user=request.user)[:10]
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def notification_create(from_user, to_user, notification_type, feed=None, comment=None):
    Notification.objects.create(
        from_user=from_user,
        to_user=to_user,
        notification_type=notification_type,
        feed=feed,
        comment=comment
    )