from django.db import models

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=50)
    page = models.TextField()

class Posts(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Message(models.Model):
    msg = models.TextField()
    priority = models.IntegerField()