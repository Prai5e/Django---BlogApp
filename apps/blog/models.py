from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class POST(models.Model):
    """ Creating model for post """

    title = models.CharField(max_length=200)
    text = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField
    published_date = models.DateTimeField

