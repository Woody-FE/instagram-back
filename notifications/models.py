from django.db import models
from django.contrib.auth import get_user_model
from articles.models import Feed, Comment

User = get_user_model()

# Create your models here.
class Notification(models.Model):

    TYPE_CHOICE = (
        ('like', 'LIKE'),
        ('comment', 'COMMENT'),
        ('follow', 'FOLLOW')
    )

    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'From: {self.from_user} - To: {self.to_user}'