from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('InReview', 'In Review'),
        ('ChangeRequested', 'Change Requested'),    
        ('Approved', 'Approved'),
        ('Published', 'Published'),
    ]
    NEWS_TYPE = [
        ('none', 'None'),
        ('LNews', 'Local News'),
        ('NNews', 'National News'),
        ('SNews', 'Sport News'),    
        ('TNews', 'Tech News'),
        ('INews', 'International News'),
        ('ENews', 'Economics News'),
        ('SANews', 'Social News'),
    ]
    title = models.CharField(max_length = 250)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='articles/image', blank=True, null=True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'Draft')
    type = models.CharField(max_length = 20, choices = NEWS_TYPE, default = 'None')
    change_requested = models.TextField(null=True, blank = True)



    def __str__(self):
     return self.title

    def get_absolute_url(self):
     return reverse('article_detail', args=[str(self.id)])
