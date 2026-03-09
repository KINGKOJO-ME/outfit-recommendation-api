from django.db import models

class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    season = models.CharField(max_length=50)

    def __str__(self):
        return self.name