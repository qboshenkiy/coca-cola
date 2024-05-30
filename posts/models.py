from django.db import models

# Create your models here.
class productViews1(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=155)
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.name

class productViews2(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=155)
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.name

class news(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.title