from django.db import models
from developer.models import Developer
from places.models import Place

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64)
    starting_price = models.IntegerField()
    delivery = models.IntegerField()
    payment_plan = models.IntegerField()
    reward = models.IntegerField()
    img_url = models.ImageField(blank=True, null=True, upload_to="images/")
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} develop by {self.developer} in {self.place}"