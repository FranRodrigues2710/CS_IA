from django.db import models

# Create your models here.

class title(models.Model):
    titles = models.TextField()
    description = models.TextField(null=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    description4 = models.TextField(null=True, blank=True)