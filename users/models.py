from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    DEPARTMENT = [
        ('none', 'None'),
        ('LNews', 'Local News'),
        ('NNews', 'National News'),
        ('SNews', 'Sport News'),    
        ('TNews', 'Tech News'),
        ('INews', 'International News'),
        ('ENews', 'Economics News'),
        ('SANews', 'Social News'),
    ]
    age = models.PositiveIntegerField(null=True, blank=True)
    department = models.CharField(max_length = 20, choices = DEPARTMENT, default = 'None')





# AbstractBaseUser vs AbstractUser
# AbstractBaseUser requires a very fine level of control and customization. We essen-
# tially rewrite Django. This can be helpful, but if we just want a custom user model
# that can be updated with additional fields, the better choice is AbstractUser which
# subclasses AbstractBaseUser . In other words, we write much less code and have less
# opportunity to mess things up. It’s the better choice unless you really know what
# you’re doing with Django!
