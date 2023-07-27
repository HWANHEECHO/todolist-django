from django.db import models

# Create your models here.

class pracclass(models.Model):
    content = models.CharField(max_length = 255)