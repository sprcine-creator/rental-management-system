
# Create your models here.
from django.db import models


class Equipment(models.Model):
    CATEGORY_CHOICES = [
        ("Light", "Light"),
        ("Grip", "Grip"),
        ("Power", "Power"),
        ("Generator", "Generator"),
        ("Accessory", "Accessory"),
        ("Other", "Other"),
    ]

    UNIT_CHOICES = [
        ("Nos", "Nos"),
        ("Set", "Set"),
        ("Pair", "Pair"),
        ("Roll", "Roll"),
    ]

    name = models.CharField(max_length=100, unique=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    unit = models.CharField(
        max_length=20,
        choices=UNIT_CHOICES,
        default="Nos"
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    standard_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    sac_code = models.CharField(
        max_length=20,
        default="998314"
    )

   
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name