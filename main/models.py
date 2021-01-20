from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Book(models.Model):
    title = models.CharField(max_length=120) 
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=650)
    price = models.IntegerField()
    genre = models.CharField(max_length=60)
    author = models.CharField(max_length=35)
    year = models.DateField()
    date = models.DateField(auto_now_add=True)

     

