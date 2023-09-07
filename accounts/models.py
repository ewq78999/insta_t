from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile',
    )
    # post_set = 
    # like_posts = 

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # followers = 