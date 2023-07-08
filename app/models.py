from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Birds(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    bird_pic=models.ImageField()
    bird_name=models.CharField(max_length=100,primary_key=True)
    about=models.TextField()

    def __str__(self) -> str:
        return self.bird_name
