from django.db import models

# Create your models here.

class news(models.Model):
    title = models.TextField()
    paragraph = models.TextField(null=True)
    paragraph2 = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    shortitle = models.TextField(null=True)