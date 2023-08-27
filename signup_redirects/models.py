from django.contrib.postgres import constraints as pgconstraints
from django.contrib.postgres import fields as pgfields
from django.db import models
from django.db.models.functions import Now


class SignupRedirectsManager(models.Manager):
    def active(self):
        return self.filter(duration__contains=Now())


class SignupRedirect(models.Model):
    class Meta:
        verbose_name = "presmerovanie"
        verbose_name_plural = "presmerovania"

        constraints = [
            pgconstraints.ExclusionConstraint(
                name="no-same-origin-overlaps",
                expressions=[
                    ("origin", pgfields.RangeOperators.EQUAL),
                    ("duration", pgfields.RangeOperators.OVERLAPS),
                ],
            ),
        ]

    name = models.CharField("Názov", max_length=512)
    origin = models.SlugField("Skrátená adresa")
    target = models.URLField("Cieľová adresa")
    duration = pgfields.DateRangeField("Trvanie")

    objects = SignupRedirectsManager()

    def __str__(self) -> str:
        return self.name
