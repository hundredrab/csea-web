from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    """
    Model for blogposts.

    Blogposts are simple, with upto a single image and a stream of html-text.
    """

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='blog/images', max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
