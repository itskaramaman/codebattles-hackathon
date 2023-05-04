from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Advocate(models.Model):
    profile_pic = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False)
    bio = models.TextField(null=True, blank=True)
    twitter = models.TextField()
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.username)
    
