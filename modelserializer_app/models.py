from django.db import models
# from django.contrib.auth.models  import User
# class Account(models.Model):
#   account_name=models.CharField(max_length=50)
#   users=models.ForeignKey(User,on_delete=models.CASCADE)
#   created=models.DateField(auto_now_add=True)
# # Create your models here.

# fields = ['url', 'id', 'account_name', 'users', 'created']
class Account(models.Model):
  account_name=models.CharField(max_length=50)
  users=models.CharField(max_length=50)
  created=models.DateField(auto_now_add=True)
  account_url=models.URLField(max_length = 200)

class HighScore(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    player_name = models.CharField(max_length=10)
    score = models.IntegerField()

  #new changes for testing- 