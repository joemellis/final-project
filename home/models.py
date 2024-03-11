from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image',default = 'placeholder')
    info = models.TextField(max_length = 500)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title