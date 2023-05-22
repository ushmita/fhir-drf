from django.db import models
from practitioners.models import Practitioners

# Create your models here.


class Qualifications(models.Model):
    code = models.CharField(max_length=100)
    period = models.IntegerField()
    issuer = models.CharField(max_length=200)
    practitioners = models.ForeignKey(
        Practitioners, on_delete=models.CASCADE, related_name='qualification')
