from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User

class Home(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    additional_photos = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   # contact_button_text = models.CharField(max_length=255, default="Contact")
    #favorites = models.ManyToManyField(User, related_name='favorite_homes', blank=True)
    

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sender: {self.sender}, Recipient: {self.recipient}, Subject: {self.subject}'