
from django.db import models
from django.contrib.auth.models import User
from django import forms


class Recipes (models.Model):
        
    def __str__(self) -> str:
        return f'{self.name}'


    name=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=1500)
    duration=models.fields.IntegerField()
    created_date=models.fields.DateTimeField(auto_now_add=True)
    updated_date=models.fields.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True)




class comments(models.Model):
    comments=models.TextField()
    recipe= models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date= models.DateTimeField(auto_now_add= True)




