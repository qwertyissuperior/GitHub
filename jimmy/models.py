from django.db import models

# Create your models here.

CATEGORIES = (
    ("Sides", "sides"),
    ("Chef's Special", "specials"),
    ("Drinks", "drinks"),
    ("Dessert", "dessert"),
)

class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORIES)

    def __str__(self):
        return self.title