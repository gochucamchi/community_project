from django.db import models

class Feed(models.Model):
    content = models.TextField()