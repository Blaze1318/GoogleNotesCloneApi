from django.db import models

# Create your models here.
class Items(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title