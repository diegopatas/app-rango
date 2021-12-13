from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    """A model of a kitchen inventory created by the user."""
    text = models.CharField(max_length=200)
    # data_added = models.DateTimeField(auto_now_add=timezone.utc)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self):
        """Return a string representation of the inventory."""
        return self.text

class Ingredient(models.Model):
    """A model of a specific type of ingredient."""
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    # data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the ingredient."""
        return self.text
#
# class Receipt(models.Model):
#     """A model of a receipt created by the user."""
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receipts')
#     body = models.TextField()
#
#     def __str__(self):
#         return self.title