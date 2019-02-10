from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name