from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# class Tags(models.Model):
#     tags = models.CharField(max_length=255)
#
#     class Meta:
#         verbose_name = 'Tag'
#         verbose_name_plural = 'Tags'
#
#     def __str__(self):
#         return self.tags


class News(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    # tags = models.ManyToManyField('Tags', related_name='tag')
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
