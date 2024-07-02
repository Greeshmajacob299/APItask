from django.db import models

# Create your models here.
class Destination(models.Model):
    placename = models.CharField(max_length=200)
    weather =models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    dest_image=models.ImageField(upload_to='tourist_dest/')
    google_map_link = models.URLField()
    description=models.TextField()