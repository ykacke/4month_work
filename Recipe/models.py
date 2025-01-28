from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('g', 'Граммы'),
        ('kg', 'Килограммы'),
        ('ml', 'Миллилитры'),
        ('l', 'Литры'),
        ('pcs', 'Штуки'),
    ]

    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)
    recipe = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.quantity} {dict(self.UNIT_CHOICES).get(self.unit)})"
