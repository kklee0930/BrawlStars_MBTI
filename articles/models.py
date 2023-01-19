from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Questions(models.Model):
    image = ProcessedImageField(
        upload_to='images',
        format='JPEG',
        processors=[ResizeToFill(500,500)],
        options={'quality': 70},
        blank=True,
        null=True)
    question = models.TextField(max_length=200)
    answer1 = models.TextField(max_length=200)
    answer2 = models.TextField(max_length=200)

class Choices(models.Model):
    I_choice = models.PositiveSmallIntegerField(default=0)
    E_choice = models.PositiveSmallIntegerField(default=0)
    S_choice = models.PositiveSmallIntegerField(default=0)
    N_choice = models.PositiveSmallIntegerField(default=0)
    T_choice = models.PositiveSmallIntegerField(default=0)
    F_choice = models.PositiveSmallIntegerField(default=0)
    P_choice = models.PositiveSmallIntegerField(default=0)
    J_choice = models.PositiveSmallIntegerField(default=0)
    
class Brawlers(models.Model):
    name = models.CharField(max_length=25)
    mbti = models.CharField(max_length=4)
    quote = models.TextField()