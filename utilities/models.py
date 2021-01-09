from django.db import models

class BaseUtility(models.Model):

    class Month(models.TextChoices):
        JANUARY = 'Jan', 'January'
        FEBRUARY = 'Feb', 'February'
        MARCH = 'Mar', 'March'
        APRIL = 'Apr', 'April'
        MAY = 'May', 'May'
        JUNE = 'Jun', 'June'
        JULY = 'Jul', 'July'
        AUGUST= 'Aug', 'August'
        SEPTEMBER = 'Sep', 'September'
        OCTOBER = 'Oct', 'October'
        NOVEMBER = 'Nov', 'November'
        DECEMBER = 'Dec', 'December'

    year = models.PositiveIntegerField(null=False, blank=False)

    month = models.CharField(
        max_length=3,
        choices=Month.choices,
        default=Month.JANUARY,
        null=False,
        blank=False,
    )

    amount = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False,)

    class Meta:
        abstract = True

class Water(BaseUtility):
    """
    Water usage
    """

    class Meta:
        verbose_name_plural = "water"


class Electricity(BaseUtility):
    """
    Prepaid electricity usage
    """

    units = models.DecimalField(max_digits=6, decimal_places=2)

    charges = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "electricity"


class Petrol(BaseUtility):
    """
    TODO
    """

    day = models.IntegerField()

    liters = models.DecimalField(max_digits=6, decimal_places=2, help_text="How many liters did you fill up with?")

    class Meta:
        verbose_name_plural = "petrol"