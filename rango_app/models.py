from django.db import models
from django.contrib.auth.models import User

class Receipt(models.Model):
    """A model of a receipt created by the user."""
    title = models.CharField(max_length=200)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receipts')
    ingredient = models.TextField()
    how_to_do = models.TextField()
    cooking_time = models.TimeField()
    total_servings = models.IntegerField()

    def __str__(self):
        return self.title