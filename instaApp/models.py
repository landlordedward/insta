from django.db import models
from django.urls import reverse

from imagekit.models import ProcessedImageField

class Post(models.Model) :
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])


class PostTwo(models.Model) :
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True
    )