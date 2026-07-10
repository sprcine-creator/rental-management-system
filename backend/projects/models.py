from django.db import models
from customers.models import Customer


class Project(models.Model):

    PROJECT_TYPES = [
        ("TV Serial", "TV Serial"),
        ("Movie", "Movie"),
        ("Advertisement", "Advertisement"),
        ("Web Series", "Web Series"),
        ("Corporate", "Corporate"),
        ("Event", "Event"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Completed", "Completed"),
        ("On Hold", "On Hold"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="projects",
    )

    project_name = models.CharField(
        max_length=200,
    )

    short_code = models.CharField(
        max_length=20,
        blank=True,
    )

    project_type = models.CharField(
        max_length=30,
        choices=PROJECT_TYPES,
    )

    start_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    billing_contact = models.CharField(
        max_length=200,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
    auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.customer.name} - {self.project_name}"