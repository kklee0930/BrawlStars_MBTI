from django.db import models
from imagekit.models import ProcessedImageField

# Create your models here.
class Questions(models.Model):
    image = ProcessedImageField(
        upload_to='images',
        blank=True,
        null=True)
    question = models.TextField(max_length=200)
    answer1 = models.TextField(max_length=200, blank=True)
    answer1_letter = models.CharField(max_length=1, blank=True)
    answer2 = models.TextField(max_length=200, blank=True)
    answer2_letter = models.CharField(max_length=1, blank=True)
    
class Brawlers(models.Model):
    name = models.CharField(max_length=25)
    image = ProcessedImageField(
        blank=True,
        null=True
    )
    mbti = models.CharField(max_length=4)
    quote = models.TextField()
    
class Visitors(models.Model):
    counts = models.PositiveIntegerField(default=1)