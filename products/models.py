from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='products',
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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

    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name