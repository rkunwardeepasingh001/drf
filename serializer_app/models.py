from django.db import models

# Create your models here.
class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField()
    def __str__(self):
        return self.email
    
    