from django.db import models

# Create your models here.
class Webtoon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    characters = models.JSONField()  # List of characters as JSON

    def __str__(self):
        return self.title