from django.db import models
#from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WTF(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag, blank=True)
    short = models.CharField(max_length=8)

    def __str__(self):
        return self.content
