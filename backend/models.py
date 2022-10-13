from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    date_joined = models.IntegerField(null=True)

    def __str__(self):
        return self.username
