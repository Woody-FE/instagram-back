from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from random import choice
import string
from time import strftime
import re

def image_path(instance, filename):
    name = ''
    for _ in range(8):
        name += choice(string.ascii_letters)
    extension = filename.split('.')[-1]
    return '{}/{}/{}.{}'.format(strftime('feeds/%Y/%m/%d'), instance.user.username, name, extension)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Feed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    content = models.CharField(max_length=140)
    tags = models.ManyToManyField(Tag, related_name="tag_feeds")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_feeds', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
 
    # def tag_save(self):
    #     tag_sets = re.findall(r'#(\w+)\b', self.content)

    #     if not tag_sets:
    #         return

    #     for t in tag_sets:
    #         tag, tag_created = Tag.objects.get_or_create(name=t)
    #         self.tags.add(tag)

    @property
    def like_count(self):
        return self.like_users.count()
    
    @property
    def comment_count(self):
        return self.comments.count()

    def __str__(self):
        return self.content

class FeedImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to=image_path, processors=[ResizeToFill(600,600)], format="JPEG", options={'quality': 100})

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    feed = models.ForeignKey(Feed, related_name='comments', on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    @property
    def comment_like_count(self):
        return self.like_users.count()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content