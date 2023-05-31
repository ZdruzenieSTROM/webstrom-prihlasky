from django.contrib.postgres import constraints as pgconstraints
from django.contrib.postgres import fields as pgfields
from django.db import models
from django.db.models.functions import Now


class SignupRedirectsManager(models.Manager):
    def active(self):
        return self.filter(duration__contains=Now())


class SignupRedirect(models.Model):
    class Meta:
        constraints = [
            pgconstraints.ExclusionConstraint(
                name="no-same-origin-overlaps",
                expressions=[
                    ("origin", pgfields.RangeOperators.EQUAL),
                    ("duration", pgfields.RangeOperators.OVERLAPS),
                ],
            ),
        ]

    name = models.CharField(max_length=512)
    origin = models.SlugField()
    target = models.URLField()
    duration = pgfields.DateRangeField()

    objects = SignupRedirectsManager()

    def __str__(self) -> str:
        return self.name
