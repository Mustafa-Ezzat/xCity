from django.db import models
from developer.models import Developer

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} develop by {self.developer}"