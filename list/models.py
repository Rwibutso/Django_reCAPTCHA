from pyexpat import model
from django.db import models

class Home(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.CharField(max_length=300)


    def __str__(self):
        return (self.tittle)