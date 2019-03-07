from django.db import models

# Create your models here.

class Portfolio(models.Model): # Class명은 항상 대문자로 시작!
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title