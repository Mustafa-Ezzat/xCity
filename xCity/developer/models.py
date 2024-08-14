from django.db import models

# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=64)
    img_url = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        return f"{self.id}: {self.name}"