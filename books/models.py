from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    content = models.TextField()


    def __str__(self) -> str:       # retorna a un string - Devuelve el "titulo" como titulo 
        return self.title

