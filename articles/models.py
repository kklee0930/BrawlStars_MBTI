from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill, resize

# Create your models here.
class Questions(models.Model):
    image = ProcessedImageField(
        upload_to='images',
        # processors=[ResizeToFit(height=230)],
        # options={'quality': 70},
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
        # processors=[ResizeToFill(width=200, height=200)],
        # options={'quality': 70},
        blank=True,
        null=True
    )
    mbti = models.CharField(max_length=4)
    quote = models.TextField()
    
class Visitors(models.Model):
    counts = models.PositiveIntegerField(default=0)