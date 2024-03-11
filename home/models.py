from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image',default = 'placeholder')
    info = models.TextField(max_length = 500)
    price =  models.CharField(max_length = 100)