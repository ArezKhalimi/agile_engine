from django.db import models


class HashTag(models.Model):
    tag_name = models.CharField(
        max_length=50,
        unique=True
    )


class Image(models.Model):
    pcid = models.CharField(
        max_length=100,
        unique=True
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    picture = models.ImageField(
        upload_to='pics',
        blank=True,
        null=True
    )
    camera = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    author = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    hashtags = models.ManyToManyField(
        HashTag,
        related_name='tags',
        blank=True,
    )
    size = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    last_activity = models.DateTimeField(
        auto_now_add=True
    )
