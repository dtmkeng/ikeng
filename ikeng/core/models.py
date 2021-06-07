from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    birtday = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    github_url = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
