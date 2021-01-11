from django.db import models

import datetime

# Create your models here.


class Rain(models.Model):
    """
    Track how main rain has fallen on a particular day
    """

    day = models.DateField(default=datetime.date.today)

    amount = models.PositiveSmallIntegerField(
        help_text="How much rain in ML was collected on the day."
    )

    hail = models.BooleanField(
        default=False,
        help_text="Whether or not it hailed during the rainfall."
    )

    class Meta:
        verbose_name_plural = "rain"
