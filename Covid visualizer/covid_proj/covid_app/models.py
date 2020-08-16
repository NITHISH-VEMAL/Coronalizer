from django.db import models

# Create your models here.

class MyModel(models.Model):

    timing = models.CharField(max_length=255)
    cases = models.BigIntegerField()

    def __str__(self):
        return self.timing

class Suggest(models.Model):
    suggestions = models.CharField(max_length=255)

    def __str__(self):
        return self.suggestions
