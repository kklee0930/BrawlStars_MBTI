from django.db import models

# Create your models here.
class Choices(models.Model):
    I_choice = models.PositiveSmallIntegerField(default=0)
    E_choice = models.PositiveSmallIntegerField(default=0)
    S_choice = models.PositiveSmallIntegerField(default=0)
    N_choice = models.PositiveSmallIntegerField(default=0)
    T_choice = models.PositiveSmallIntegerField(default=0)
    F_choice = models.PositiveSmallIntegerField(default=0)
    P_choice = models.PositiveSmallIntegerField(default=0)
    J_choice = models.PositiveSmallIntegerField(default=0)