from django.db import models

from projects.models import Project
from equipment.models import Equipment


class CommercialRate(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="commercial_rates",
    )

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
    )

    negotiated_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    remarks = models.CharField(
        max_length=200,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        unique_together = (
            "project",
            "equipment",
        )

    def __str__(self):

        return f"{self.project.project_name} - {self.equipment.name}"