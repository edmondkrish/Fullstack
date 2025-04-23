from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.TextField()
    published_date = models.DateField(null=True, blank=True) 
    url=models.URLField(blank=True)

    def __str__(self):
        return self.name 
