from django.db import models
#from django.contrib.auth.models import User

class WTF(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)
    tags = models.CharField(max_length=100)
    short = models.CharField(max_length=8)

    def __str__(self):
        return self.email
