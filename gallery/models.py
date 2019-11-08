from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    title = models.CharField(max_length=30)


class Image(models.Model):
    image = models.ImageField(upload_to='profile_pics')
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

