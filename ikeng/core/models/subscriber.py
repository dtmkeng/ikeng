from django.db import models


class SubscriberModel(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscriber"
