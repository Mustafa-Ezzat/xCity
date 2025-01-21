from django.db import models
from developer.models import Developer
from places.models import Place

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} develop by {self.developer}"