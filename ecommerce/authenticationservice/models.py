from django.db import models
from django.contrib.auth.models import AbstractUser 
from ecommerce.basemodels import TimeStampedModel

class User(AbstractUser, TimeStampedModel): 
    def __str__(self):
        return self.username 
