from django.db import models

# Create your models here.
class Cheese(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    tasting_notes = models.TextField()
    user = models.ForeignKey('auth.User', related_name='cheeses', on_delete=models.CASCADE)
