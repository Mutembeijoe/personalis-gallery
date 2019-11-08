from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='profile_pics')
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
