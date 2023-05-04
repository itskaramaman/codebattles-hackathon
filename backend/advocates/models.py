from django.db import models


class Advocate(models.Model):
    profile_pic = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False)
    bio = models.TextField(null=True, blank=True)
    twitter = models.TextField()

    def __str__(self):
        return str(self.username)
    
