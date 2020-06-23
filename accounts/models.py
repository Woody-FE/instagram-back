from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def photo_path(instance, filename):
    return f'profiles/{instance.username}/{filename}'

# Create your models here.
class User(AbstractUser):

    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
    }

    name = models.CharField("사용자이름", max_length=100, blank=True)
    profile_photo = ProcessedImageField(upload_to=photo_path, processors=[ResizeToFill(150, 150)], format='JPEG', options={'quality': 100}, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.username

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()

    # def get_absolute_url(self):
    #     return reverse()
