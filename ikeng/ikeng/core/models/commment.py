from django.db import models
from ikeng.core.models import Post


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="comment",
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=300)
