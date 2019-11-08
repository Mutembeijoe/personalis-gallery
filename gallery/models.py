from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images_gallery')
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

