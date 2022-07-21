from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)  # note: FK in real life

    def __str__(self):
        return self.name