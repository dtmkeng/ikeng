from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=300)

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="comment",
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=300)
